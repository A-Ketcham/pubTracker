# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0010_auto_20150410_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplan',
            name='approved',
            field=models.NullBooleanField(default=None, max_length=3, choices=[(None, b''), (True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
