# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-06 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('help4vzl', '0006_auto_20180906_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulation',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='help4vzl.Organization'),
        ),
    ]