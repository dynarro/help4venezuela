# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostulationForm
from .models import Postulation

def postulation(request):
    return render(request, 'help4vzl/postulation.html', {})

def postulation_new(request):
    if request.method == "POST":
        form = PostulationForm(request.POST)
        if form.is_valid():
                postulation = form.save(commit=False)
                postulation.save()
                return redirect('postulation_detail', pk=postulation.pk)
    else:
        form = PostulationForm()
    return render(request, 'help4vzl/postulation_edit.html', {'form': form})

def postulation_detail(request, pk):
    postulation = get_object_or_404(Postulation, pk=pk)
    return render(request, 'help4vzl/postulation_detail.html', {'postulation': postulation})

def postulation_edit(request, pk):
 postulation = get_object_or_404(Postulation, pk=pk)
 if request.method == "POST":
     form = PostulationForm(request.POST, request.FILES or None, instance=postulation)
     if form.is_valid():
          postulation = form.save(commit=False)
          postulation.save()
          return redirect('postulation_detail', pk=postulation.pk)
 else:
     form = PostulationForm(instance=postulation)
 return render(request, 'help4vzl/postulation_edit.html', {'form': form})
