# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('item_name', models.CharField(max_length=30, verbose_name=b'Item Name')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('price', models.DecimalField(null=True, verbose_name=b'Price', max_digits=3, decimal_places=2, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('type_name', models.CharField(max_length=30, verbose_name=b'Type Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('md5', models.CharField(max_length=50, serialize=False, verbose_name=b'md5', primary_key=True)),
                ('rating', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Rating', choices=[(b'2', b'Like'), (b'3', b'Super Like'), (b'1', b'Not Like')])),
                ('why', models.CharField(max_length=255, null=True, blank=True)),
                ('imp', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Creation Date')),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Creation Date')),
                ('menu', models.ForeignKey(verbose_name=b'Menu Name', to='management.MenuCard')),
                ('menu_type', models.ForeignKey(verbose_name=b'Menu For', to='management.MenuType')),
                ('vendor', models.ForeignKey(verbose_name=b'Vendor', to='management.Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorMenuType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('menu_type', models.ForeignKey(verbose_name=b'Menu For', to='management.MenuType')),
                ('vendor', models.ForeignKey(verbose_name=b'Vendor', to='management.Vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='userrating',
            name='vendor',
            field=models.ForeignKey(verbose_name=b'Vendor', blank=True, to='management.Vendor', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='vendormenu',
            unique_together=set([('menu', 'vendor')]),
        ),
    ]
