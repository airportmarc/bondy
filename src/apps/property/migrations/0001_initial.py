# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-12 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Contact')),
                ('mls', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.contact',),
        ),
    ]
