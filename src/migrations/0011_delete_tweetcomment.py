# Generated by Django 2.2 on 2021-05-08 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0010_auto_20210503_1845'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TweetComment',
        ),
    ]