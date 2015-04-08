# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20150403_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonPOV',
            fields=[
                ('transportation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='forms.Transportation')),
                ('type', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=('forms.transportation',),
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('transportation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='forms.Transportation')),
                ('flightID', models.CharField(max_length=10)),
                ('flightDate', models.DateTimeField()),
                ('airportCode', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=('forms.transportation',),
        ),
        migrations.CreateModel(
            name='POV',
            fields=[
                ('transportation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='forms.Transportation')),
                ('licenseNum', models.CharField(max_length=10)),
                ('make', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=('forms.transportation',),
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('transportation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='forms.Transportation')),
                ('station', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=('forms.transportation',),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='transpoType',
            field=models.CharField(max_length=10, choices=[(b'A', b'Plane'), (b'B', b'Train'), (b'C', b'POV'), (b'D', b'Non-POV')]),
            preserve_default=True,
        ),
    ]
