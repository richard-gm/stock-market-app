# Generated by Django 2.2 on 2021-03-25 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
    ]
