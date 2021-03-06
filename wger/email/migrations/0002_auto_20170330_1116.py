# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-30 08:16
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('email', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='log',
            name='gym',
            field=models.ForeignKey(editable=False,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='email_log', to='gym.Gym'),
        ),
    ]
