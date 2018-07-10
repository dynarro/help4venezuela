# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categories,Cases,Postulation, Organization, OrganizationUser, Collaborator
# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_filter=('name',)


@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    list_display=('category','description','attachments',)
    list_filter=('category',)


@admin.register(Postulation)
class PostulationAdmin(admin.ModelAdmin):
    list_display=('name','motivation','status',)
    list_filter=('name','status',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display=('name','email','description',)
    list_filter=('name',)
