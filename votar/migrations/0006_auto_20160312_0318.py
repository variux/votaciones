# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votar', '0005_auto_20160312_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
