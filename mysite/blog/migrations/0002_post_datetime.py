# Generated by Django 2.2.4 on 2019-08-06 13:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 6, 13, 53, 19, 369703, tzinfo=utc), verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]
