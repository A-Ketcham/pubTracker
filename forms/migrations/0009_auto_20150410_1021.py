# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20150409_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='cadet',
            name='lastName',
        ),
        migrations.AddField(
            model_name='travelplan',
            name='approved',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
