# Generated by Django 2.2.11 on 2020-04-15 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community_centers',
            options={'verbose_name_plural': 'community_centers'},
        ),
        migrations.AlterModelOptions(
            name='dog_gardens',
            options={'verbose_name_plural': 'dog_gardens'},
        ),
        migrations.AlterModelOptions(
            name='elderly_social_club',
            options={'verbose_name_plural': 'elderly_social_club'},
        ),
        migrations.AlterModelOptions(
            name='playgrounds',
            options={'verbose_name_plural': 'play_grounds'},
        ),
        migrations.AlterModelOptions(
            name='sport_facilities',
            options={'verbose_name_plural': 'sport_facilities'},
        ),
        migrations.AlterModelOptions(
            name='urban_nature',
            options={'verbose_name_plural': 'urban_nature'},
        ),
        migrations.AlterModelTable(
            name='playgrounds',
            table='play_grounds',
        ),
    ]
