# Generated by Django 2.2.11 on 2020-04-15 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20200415_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community_centers',
            options={'verbose_name_plural': 'community centers'},
        ),
        migrations.AlterModelOptions(
            name='dog_gardens',
            options={'verbose_name_plural': 'dog gardens'},
        ),
        migrations.AlterModelOptions(
            name='elderly_social_club',
            options={'verbose_name_plural': 'elderly social clubs'},
        ),
        migrations.AlterModelOptions(
            name='playgrounds',
            options={'verbose_name_plural': 'play grounds'},
        ),
        migrations.AlterModelOptions(
            name='sport_facilities',
            options={'verbose_name_plural': 'sport facilities'},
        ),
        migrations.AlterModelOptions(
            name='urban_nature',
            options={'verbose_name_plural': 'urban nature'},
        ),
    ]