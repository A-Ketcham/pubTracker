# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='userID',
        ),
        migrations.AddField(
            model_name='cadet',
            name='email',
            field=models.EmailField(default=b'ash.ketchum@pokemon.com', unique=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='travelplan',
            name='editDate',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.ForeignKey(to='forms.Cadet'),
            preserve_default=True,
        ),
    ]
