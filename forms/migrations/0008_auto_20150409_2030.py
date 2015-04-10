# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20150409_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='airportCode',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
    ]
