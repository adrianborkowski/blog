# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0004_auto_20161002_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
