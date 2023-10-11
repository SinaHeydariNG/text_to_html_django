# Generated by Django 4.2.6 on 2023-10-11 08:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Blog Title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
