# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length='100')),
                ('location', models.CharField(max_length='200')),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('time_zone', models.CharField(null=True, blank=True, max_length='100')),
                ('updated_time', models.DateTimeField(null=True, blank=True)),
                ('privacy', models.CharField(max_length='100')),
                ('is_date_only', models.BooleanField()),
                ('fb_id', models.CharField(max_length='100')),
            ],
            options={
                'get_latest_by': 'start_time',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length='100')),
                ('description', models.TextField()),
                ('cuisine', models.CharField(max_length='200')),
                ('vendor_type', models.CharField(choices=[('TRUCK', 'truck'), ('CART', 'cart'), ('TENT', 'tent')], default='TRUCK', max_length=25)),
                ('logo', models.CharField(null=True, blank=True, max_length=1000)),
                ('website', models.CharField(null=True, blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='vendors',
            field=models.ManyToManyField(to='comida.Vendor'),
        ),
    ]
