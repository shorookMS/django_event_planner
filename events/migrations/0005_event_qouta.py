# Generated by Django 2.1 on 2018-10-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_bookedevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='qouta',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
