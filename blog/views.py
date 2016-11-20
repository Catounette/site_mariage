from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Guest
from blog.forms import ContactForm


def home(request):

    return render(request,'blog/home.html')

def infoPratiques(request):

    return render(request,'blog/infoPratiques.html')

def transportEtAcces(request):

    return render(request,'blog/transportEtAcces.html')

def logement(request):

    return render(request,'blog/logement.html')

def nounou(request):

    return render(request,'blog/nounou.html')

def accueil(request):
    """ Afficher tous les articles de notre blog """
    guests = Guest.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_guests': guests})



def tpl(request):
    return render(request,'blog/tpl.html',{'current_date':datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1)+int(nombre2)
    return render(request,'blog/addition.html',locals())


from blog.forms import GuestForm

def adresse(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.nom= request.user
            guest.save()
            envoi=True
    else:
       form = GuestForm()

    return render(request, 'blog/guest_edit.html', locals())


