# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('item', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(default=b'veg', max_length=10, choices=[(b'veg', b'Veg'), (b'non-veg', b'Non Veg')])),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(default=b'lunch', max_length=10, choices=[(b'breakfast', b'Breakfast'), (b'lunch', b'Lunch'), (b'snacks', b'Snacks'), (b'dinner', b'Dinner')])),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('employee_id', models.CharField(max_length=10)),
                ('rating', models.IntegerField(choices=[(b'1', b'Bad'), (b'2', b'Neutral'), (b'3', b'Average'), (b'4', b'Good')])),
                ('comments', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(to='apis.Location')),
            ],
        ),
        migrations.CreateModel(
            name='VendorMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(to='apis.Service')),
                ('vendor', models.ForeignKey(to='apis.Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorMenuItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('food_item', models.ForeignKey(to='apis.FoodItems')),
                ('vendor_menu', models.ForeignKey(to='apis.VendorMenu')),
            ],
        ),
        migrations.AddField(
            model_name='userrating',
            name='vendor',
            field=models.ForeignKey(to='apis.Vendor'),
        ),
    ]
