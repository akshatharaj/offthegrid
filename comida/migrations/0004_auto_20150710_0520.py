# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0003_auto_20150709_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fb_id',
            field=models.CharField(db_index=True, max_length='100'),
        ),
    ]
