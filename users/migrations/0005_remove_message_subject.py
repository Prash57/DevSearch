# Generated by Django 3.2.11 on 2022-01-22 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
    ]
