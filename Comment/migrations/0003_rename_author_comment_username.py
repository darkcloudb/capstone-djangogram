# Generated by Django 3.2.8 on 2021-10-08 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0002_rename_username_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='username',
        ),
    ]
