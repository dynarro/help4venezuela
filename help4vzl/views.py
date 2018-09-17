# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostulationForm
from .models import Postulation, Categorie
from django.contrib.sites.shortcuts import get_current_site



def postulation(request):
    return render(request, 'help4vzl/postulation.html', {})

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

def postulation_edit(request, pk):
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
        postulation = get_object_or_404(Postulation, pk=pk)
        if postulation.organization.pk == request.user.organization_user.organization.id:
            form = PostulationForm(instance=postulation)
            return render(request, 'help4vzl/postulation_edit.html', {'form': form, 'postulation': postulation})
        else:
            raise Http404("Invalid postulation for this user")

def category_list(request):
    categories = Categorie.objects.all()
    return render(request, 'help4vzl/category_list.html', {'categories':categories})
