# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190412_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='fb',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='insta',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='twitter',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
