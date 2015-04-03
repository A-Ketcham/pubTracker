# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadet',
            fields=[
                ('xNumber', models.IntegerField(max_length=5, unique=True, serialize=False, primary_key=True)),
                ('lastName', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=25)),
                ('regiment', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4')])),
                ('company', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'F', b'F'), (b'G', b'G'), (b'H', b'H'), (b'I', b'I')])),
                ('year', models.IntegerField(max_length=4)),
                ('phone', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('transpoID', models.AutoField(serialize=False, primary_key=True)),
                ('departTime', models.DateTimeField()),
                ('transpoType', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('travelID', models.AutoField(serialize=False, primary_key=True)),
                ('destinationAdd', models.CharField(max_length=55)),
                ('transpoID', models.ForeignKey(to='forms.Transportation')),
                ('xNumber', models.ForeignKey(to='forms.Cadet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userID', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.SlugField()),
                ('case', models.CharField(max_length=10, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZIP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.IntegerField(unique=True, max_length=9)),
                ('city', models.CharField(max_length=22)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='zip',
            field=models.ForeignKey(to='forms.ZIP'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadet',
            name='userID',
            field=models.ForeignKey(to='forms.Users'),
            preserve_default=True,
        ),
    ]
