# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='location',
        ),
        migrations.AddField(
            model_name='vendor',
            name='location',
            field=models.ManyToManyField(to='apis.Location'),
        ),
    ]
