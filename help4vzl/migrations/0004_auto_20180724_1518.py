# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help4vzl', '0003_auto_20180724_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulation',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='postulation',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]