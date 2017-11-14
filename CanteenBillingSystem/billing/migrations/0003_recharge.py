# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_customer_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('worth', models.IntegerField()),
                ('used', models.BooleanField(default=False)),
            ],
        ),
    ]
