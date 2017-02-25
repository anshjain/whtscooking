# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20170225_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendormenu',
            name='location',
            field=models.ManyToManyField(to='apis.Location'),
        ),
    ]
