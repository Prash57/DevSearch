# Generated by Django 3.2.11 on 2022-03-06 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_message_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]