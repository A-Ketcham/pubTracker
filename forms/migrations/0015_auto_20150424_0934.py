# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0014_auto_20150410_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=b'1112223334', max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='xNumber',
            field=models.CharField(default=b'x00000', unique=True, max_length=6, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(default=b'0000', max_length=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='xNumber',
            field=models.ForeignKey(to='forms.UserProfile'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Cadet',
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='zip',
            field=models.ForeignKey(default=b'000010000', blank=True, to='forms.ZIP'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.CharField(default=b'A', max_length=1, blank=True, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'F', b'F'), (b'G', b'G'), (b'H', b'H'), (b'I', b'I')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='regiment',
            field=models.CharField(default=b'1', max_length=1, blank=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4')]),
            preserve_default=True,
        ),
    ]
