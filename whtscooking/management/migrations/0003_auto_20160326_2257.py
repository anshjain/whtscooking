# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20160326_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormenu',
            name='create_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'Creation Date'),
        ),
    ]
