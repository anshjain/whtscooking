# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20170225_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditems',
            name='created_at',
            field=models.DateField(auto_created=True),
        ),
    ]
