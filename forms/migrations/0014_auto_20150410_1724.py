# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0013_auto_20150410_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zip',
            name='zip',
            field=models.IntegerField(max_length=9),
            preserve_default=True,
        ),
    ]
