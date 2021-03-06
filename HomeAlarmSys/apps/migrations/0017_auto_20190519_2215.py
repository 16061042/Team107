# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_auto_20190519_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.IntegerField(default=0, verbose_name='设备类型'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='action_value',
            field=models.BooleanField(default=False, verbose_name='动作值'),
        ),
    ]
