# Generated by Django 3.2.11 on 2022-02-27 11:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
