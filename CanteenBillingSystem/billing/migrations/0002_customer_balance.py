# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]