# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0015_auto_20150424_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='departTime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
