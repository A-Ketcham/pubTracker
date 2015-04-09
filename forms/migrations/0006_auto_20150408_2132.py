# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20150407_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
