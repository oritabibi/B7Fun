# Generated by Django 2.2.11 on 2020-04-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_auto_20200426_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_centers',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
