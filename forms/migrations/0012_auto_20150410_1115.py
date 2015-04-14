# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_auto_20150410_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplan',
            name='approved',
            field=models.BooleanField(default=None, max_length=3, choices=[(None, b'No'), (True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
