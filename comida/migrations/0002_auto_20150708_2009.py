# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(default='Trucks', max_length=25),
        ),
    ]
