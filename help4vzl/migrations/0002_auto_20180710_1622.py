# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 16:22
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help4vzl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes_available', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='organization_user',
            name='Organization',
        ),
        migrations.RemoveField(
            model_name='organization_user',
            name='user',
        ),
        migrations.AddField(
            model_name='cases',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='help4vzl.Organization'),
        ),
        migrations.AddField(
            model_name='cases',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('APROVED', 'Aproved'), ('PENDING', 'Pending'), ('REJECTED', 'Rejected')], default='NEW', max_length=10),
        ),
        migrations.AddField(
            model_name='organization',
            name='phone_number',
            field=models.CharField(default=0, max_length=13),
        ),
        migrations.AddField(
            model_name='postulation',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/%Y'),
        ),
        migrations.AddField(
            model_name='postulation',
            name='phone_number',
            field=models.CharField(default=0, max_length=13),
        ),
        migrations.DeleteModel(
            name='Organization_User',
        ),
        migrations.AddField(
            model_name='organizationuser',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help4vzl.Organization'),
        ),
        migrations.AddField(
            model_name='organizationuser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
