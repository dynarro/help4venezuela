# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-06 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help4vzl', '0005_auto_20180731_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('APROVED', 'Aproved'), ('PENDING', 'Pending'), ('REVIEWED', 'Reviewed'), ('REJECTED', 'Rejected')], default='NEW', max_length=10),
        ),
        migrations.AlterField(
            model_name='postulation',
            name='status',
            field=models.CharField(choices=[('APROVED', 'Aproved'), ('PENDING', 'Pending'), ('REVIEWED', 'Reviewed'), ('REJECTED', 'Rejected')], default='PENDING', max_length=10),
        ),
    ]