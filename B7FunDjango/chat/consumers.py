# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-branches
# pylint: disable=arguments-differ
# pylint: disable=attribute-defined-outside-init
# pylint: disable=unused-argument

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from accounts.models import User
from feed.models import community_centers, dog_gardens, elderly_social_club, playgrounds, sport_facilities, urban_nature
from .models import ChatMessage


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_type = self.scope['url_route']['kwargs']['room_type']
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_name = str(self.room_type) + str(self.room_id)
        self.room_group_name = 'chat_%s' % self.room_name

        if self.room_type == "community_centers":
            if len(community_centers.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "dog_gardens":
            if len(dog_gardens.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "elderly_social_club":
            if len(elderly_social_club.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "playgrounds":
            if len(playgrounds.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "sport_facilities":
            if len(sport_facilities.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "urban_nature":
            if len(urban_nature.objects.filter(id=self.room_id)) != 1:
                return self.close()
        else:
            return self.close()

        # Join room group
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        return self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.commands[text_data_json['command']](self, text_data_json)


    def fetch_messages(self, text_data_json):
        index = text_data_json['index']
        messages = ChatMessage.objects.filter(chat_room_id=self.room_id,
                                              chat_room_type=self.room_type).order_by('-date')[(index*30):((index+1)*30)]
        messages_list = []

        for i in messages:
            messages_list += [{
                'message': i.message,
                'sender': i.sender_email,
                'date': i.date.strftime('%d/%m/%Y'),
                'time': i.date.strftime('%H:%M'),
                'profile_image': User.objects.filter(email=i.sender_email)[0].profile_image.name
            }]

        self.send(text_data=json.dumps({
            'messages': messages_list,
            'command': 'fetch_messages',
            'scroll_to_end': text_data_json['scroll_to_end']
        }))

    def send_chat_messages(self, text_data_json):
        message = text_data_json['message']
        new_message = ChatMessage(message=message, sender_email=self.scope['user'].email, chat_room_id=self.room_id,
                                  chat_room_type=self.room_type)
        new_message.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.scope['user'].email,
                'date': new_message.date.strftime('%d/%m/%Y'),
                'time': new_message.date.strftime('%H:%M'),
                'profile_image': self.scope['user'].profile_image.name,
                'command': 'new_messages'
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        date = event['date']
        time = event['time']
        profile_image = event['profile_image']
        command = event['command']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'date': date,
            'time': time,
            'profile_image': profile_image,
            'command': command
        }))

    commands = {'fetch_messages' : fetch_messages, 'new_messages': send_chat_messages}