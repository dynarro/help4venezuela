# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.db import models

class Categories(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True, blank=True)

class Cases(models.Model):
    category=models.ForeignKey(Categories, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    attachments=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

class Postulation(models.Model):
    name=models.CharField(max_length=50)
    motivation=models.TextField(null=True, blank=True)
    STATUS_CHOICES=(
        ('APROVED','Aproved'),
        ('PENDING','Pending'),
        ('REJECTED','Rejected'),
        )
    status=models.CharField(choices=STATUS_CHOICES, default='PENDING', max_length=10)

class Organization(models.Model):
    name=models.CharField(max_length=100)
    email=forms.EmailField()
    description=models.TextField(blank=True, null=True)
    logo=models.ImageField(null=True, blank=True, upload_to="logos/%Y")

class Organization_User(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Organization=models.OneToOneField(Organization, primary_key=True)
