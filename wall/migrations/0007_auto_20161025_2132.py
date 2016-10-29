# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0006_remove_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='/blog/'),
        ),
    ]