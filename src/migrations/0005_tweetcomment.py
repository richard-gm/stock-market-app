# Generated by Django 2.2 on 2021-04-04 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('src', '0004_auto_20210328_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]