# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models import IntegerField
from django.core.validators import MinValueValidator, MaxValueValidator


class Categories(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True, blank=True)

class Cases(models.Model):
    category=models.ForeignKey(Categories, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    attachments=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    organization=models.ForeignKey('Organization', null=True, blank=True)
    STATUS_CHOICES=(
        ('NEW', 'New'),
        ('APROVED','Aproved'),
        ('PENDING','Pending'),
        ('REJECTED','Rejected'),
        )
    status=models.CharField(choices=STATUS_CHOICES, default='NEW', max_length=10)

class Postulation(models.Model):
    name=models.CharField(max_length=50)
    email=forms.EmailField()
    phone_number=models.CharField(max_length=13, default=0)
    logo=models.ImageField(null=True, blank=True, upload_to="logos/%Y")
    motivation=models.TextField(null=True, blank=True)
    attachments=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    STATUS_CHOICES=(
        ('APROVED','Aproved'),
        ('PENDING','Pending'),
        ('REJECTED','Rejected'),
        )
    status=models.CharField(choices=STATUS_CHOICES, default='PENDING', max_length=10)

class Organization(models.Model):
    name=models.CharField(max_length=100)
    email=forms.EmailField()
    phone_number=models.CharField(max_length=13, default=0)
    logo=models.ImageField(null=True, blank=True, upload_to="logos/%Y")
    description=models.TextField(blank=True, null=True)

class OrganizationUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    organization=models.ForeignKey(Organization)

class Collaborator(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    votes_available=IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(5)])
