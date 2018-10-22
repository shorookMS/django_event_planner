# Generated by Django 2.1 on 2018-10-21 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20181021_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 21, 12, 36, 9, 967517, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 10, 21, 12, 36, 29, 349729, tzinfo=utc)),
            preserve_default=False,
        ),
    ]