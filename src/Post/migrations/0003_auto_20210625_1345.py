# Generated by Django 3.1.7 on 2021-06-25 12:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20210623_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 25, 12, 45, 26, 252704, tzinfo=utc)),
        ),
    ]
