# Generated by Django 3.2.8 on 2021-10-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimg',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postimg',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
