# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_auto_20150410_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='company',
        ),
        migrations.RemoveField(
            model_name='cadet',
            name='regiment',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'F', b'F'), (b'G', b'G'), (b'H', b'H'), (b'I', b'I')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='regiment',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='approved',
            field=models.NullBooleanField(default=False, max_length=3, choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
