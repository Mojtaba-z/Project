# Generated by Django 2.2.5 on 2019-10-20 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
