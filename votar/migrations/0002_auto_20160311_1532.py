# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='cedula',
            field=models.IntegerField(),
        ),
    ]
