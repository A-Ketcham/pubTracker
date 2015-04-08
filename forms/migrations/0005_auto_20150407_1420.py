# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20150405_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadet',
            name='email',
            field=models.EmailField(default=b'ash.ketchum@usma.com', unique=True, max_length=254),
            preserve_default=True,
        ),
    ]
