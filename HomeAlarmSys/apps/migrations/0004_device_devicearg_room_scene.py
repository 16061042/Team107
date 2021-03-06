# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20190424_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='设备')),
                ('enable', models.CharField(max_length=20, verbose_name='能否使用')),
            ],
            options={
                'verbose_name': '设备',
                'verbose_name_plural': '设备',
            },
        ),
        migrations.CreateModel(
            name='DeviceArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=20, verbose_name='设备id')),
                ('arg_name', models.CharField(max_length=20, verbose_name='参数名称')),
                ('value', models.IntegerField(verbose_name='参数值')),
            ],
            options={
                'verbose_name': '设备参数',
                'verbose_name_plural': '设备参数',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20, verbose_name='房间名称')),
            ],
            options={
                'verbose_name': '房间',
                'verbose_name_plural': '房间',
            },
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.CharField(max_length=20, verbose_name='场景名称')),
            ],
            options={
                'verbose_name': '场景',
                'verbose_name_plural': '场景',
            },
        ),
    ]
