# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votar', '0007_auto_20160312_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='gender',
            field=models.IntegerField(null=True),
        ),
    ]
