# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0007_auto_20161025_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='/blog/'),
        ),
    ]