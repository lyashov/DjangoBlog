# Generated by Django 2.2.4 on 2019-08-06 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='datetime',
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 6, 13, 58, 38, 793015, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
