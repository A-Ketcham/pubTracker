# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20150403_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='case',
            field=models.CharField(max_length=10, null=True, choices=[(b'A', b'Admin'), (b'T', b'TAC'), (b'S', b'Cadet S1')]),
            preserve_default=True,
        ),
    ]
