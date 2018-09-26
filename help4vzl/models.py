# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django import forms
from django.db import models
from django.db.models import IntegerField
from django.template.loader import render_to_string
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.mail import BadHeaderError, send_mail, mail_admins


class Categorie(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True, blank=True)

class Case(models.Model):
    category=models.ForeignKey(Categorie, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    attachments=models.FileField(null=True, blank=True, upload_to='documents/%Y')
    organization=models.ForeignKey('Organization', null=True, blank=True)
    STATUS_CHOICES=(
        ('NEW', 'New'),
        ('APROVED','Aproved'),
        ('PENDING','Pending'),
        ('REVIEWED','Reviewed'),
        ('REJECTED','Rejected'),
        )
    status=models.CharField(choices=STATUS_CHOICES, default='NEW', max_length=10)

def send_postulation_status_email(postulation):
    full_url = ''.join(['http://', Site.objects.get_current().domain])
    from_email = settings.EMAIL_HOST_USER
    to = [postulation.email]
    subject = 'Congratulations creating your postulation'
    html_message = render_to_string('help4vzl/email.html', {'postulation': postulation, 'domain':full_url})
    plain_message = "Congratulations! You have just created your postulation. You can now make modifications to your postulation if you think it's needed by going to this link: "

    if postulation.status == "NEW":
        mail_admins('A new postulation has been created','Hey! A new postulation has been created')

    if  postulation.status == 'PENDING':
        send_mail(subject, "Congratulations!You have just created your postulation. You can now make modifications to your postulation if you think it's needed",from_email, to, html_message=html_message, fail_silently=True)

    if postulation.status == 'REVIEWED':
        send_mail('Your postulation has been reviewed', "Your postulation has been reviewed.You won't be able to apply other modifications to your postulation ",from_email, to,fail_silently=True)

    if postulation.status == 'APPROVED':
        send_mail('Your postularion has been approved', "Congratulations, your postulation has been approved.",from_email, to, fail_silently=True)

    if postulation.status =='REJECTED':
        send_mail('Your postulation has been rejected', "Sorry, your postulation has been rejected.If you think this is a mistake, please contact us.",from_email, to, fail_silently=True)
    else:
        pass

def create_organization_user(org):
    (user, created) = User.objects.get_or_create(username=org.email, email=org.email)
    (org_user, created) = OrganizationUser.objects.get_or_create(user=user,
                                                                 organization=org,)

# Creates an organization when the postulation status isn't new
def create_organization(postulation):
    (org, created)= Organization.objects.get_or_create(name=postulation.name,
                                                       email=postulation.email,
                                                       )
    org.phone_number=postulation.phone_number
    org.logo=postulation.logo
    org.description=postulation.motivation
    org.save()
    create_organization_user(org)
    return org

class Postulation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True)
    phone_number=models.CharField(max_length=13)
    logo=models.ImageField(null=True, blank=True, upload_to="logos/%Y")
    motivation=models.TextField(null=True, blank=True)
    attachments=models.FileField(null=True, blank=True, upload_to='documents/%Y')
    organization=models.ForeignKey('Organization', null=True, blank=True)
    STATUS_CHOICES=(
        ('NEW','New'),
        ('PENDING','Pending'),
        ('REVIEWED','Reviewed'),
        ('APROVED','Aproved'),
        ('REJECTED','Rejected'),

        )
    status=models.CharField(choices=STATUS_CHOICES, default='NEW', max_length=10)
# the save method calls the `send_postulation_status_email` functions
# when a postulation is created.
    def save(self, *args, **kwargs):
        if self.status != 'NEW':
            org=create_organization(self)
            if org is not None:
                self.organization=org

        super(Postulation, self).save(*args, **kwargs)  # Call the "real" save() method.
        send_postulation_status_email(self)


class Organization(models.Model):
    name=models.CharField(max_length=10, unique=True)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=13, default=0)
    logo=models.ImageField(null=True, blank=True, upload_to="logos/%Y")
    description=models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class OrganizationUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    organization=models.ForeignKey('Organization',null=True, blank=True)

class Collaborator(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    votes_available=IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(5)])
