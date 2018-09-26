# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categorie,Case,Postulation, Organization, OrganizationUser, Collaborator
# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_filter=('name',)


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display=('category','description','attachments',)
    list_filter=('category',)


@admin.register(Postulation)
class PostulationAdmin(admin.ModelAdmin):
    list_display=('name','email','status',)
    list_filter=('name','status',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display=('name','email','description',)
    list_filter=('name',)

@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    list_display=('user', 'organization',)
    list_filter=('user', 'organization',)
