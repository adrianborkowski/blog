# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 18:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 9, 29)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lon',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
