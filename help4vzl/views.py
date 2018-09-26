# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostulationForm
from .models import Postulation, Categorie, OrganizationUser
from django.contrib.sites.shortcuts import get_current_site



def postulation(request):
    if request.user.is_authenticated:
        org_user = OrganizationUser.objects.get(user=request.user)
        postulation = Postulation.objects.get(organization=org_user.organization)
        return render(request, 'help4vzl/postulation.html', {'postulation':postulation})
    else:
        return render(request, 'help4vzl/postulation.html')
def postulation_new(request):
    if request.method == "POST":
        form = PostulationForm(request.POST)
        if form.is_valid():
                postulation = form.save(commit=False)
                postulation.save()
                #return redirect('postulation_detail', pk=postulation.pk)
                return redirect('thankyoupage')
    else:
        form = PostulationForm()
    return render(request, 'help4vzl/postulation_edit.html', {'form': form})

def postulation_detail(request, pk):
    postulation = get_object_or_404(Postulation, pk=pk)
    return render(request, 'help4vzl/postulation_detail.html', {'postulation': postulation})

def thankyoupage(request):
    return render(request, 'help4vzl/thankyoupage.html')

@login_required(login_url="login/")
def postulation_edit(request, pk):
    postulation = get_object_or_404(Postulation, pk=pk)
    if request.method == "POST":
        form = PostulationForm(request.POST, request.FILES or None, instance=postulation)
        if form.is_valid():
            postulation = form.save(commit=False)
            postulation.save()
            if request.user.is_authenticated():
                return redirect('postulation_detail', pk=postulation.pk)
            else:
                return redirect('thankyoupage')
    else:
        #user = request.user
        if postulation.organization.pk == OrganizationUser.objects.get(user=request.user).organization.pk:
            form = PostulationForm(instance=postulation)
            return render(request, 'help4vzl/postulation_edit.html', {'form': form, 'postulation': postulation})
        else:
            raise Http404("Invalid postulation for this user")

def logout_user(request):
    logout(request)
    return redirect('login')


def category_list(request):
    categories = Categorie.objects.all()
    return render(request, 'help4vzl/category_list.html', {'categories':categories})
