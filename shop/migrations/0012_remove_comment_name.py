# Generated by Django 2.2.5 on 2019-10-21 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
