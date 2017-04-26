# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-26 09:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_userfitbitdetails_userfitbitscope'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfitbitdetails',
            name='fitbit_user_id',
            field=models.CharField(default=datetime.datetime(2017, 4, 26, 9, 4, 0, 800005, tzinfo=utc), max_length=400, unique=True),
            preserve_default=False,
        ),
    ]