# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_vendormenu_location'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vendormenu',
            unique_together=set([('vendor', 'service')]),
        ),
    ]
