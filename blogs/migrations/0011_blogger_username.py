# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_remove_blogger_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='username',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
