from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from . import views


urlpatterns = [

    url(r'^home$', views.home, name='home'),
    url(r'^infoPratiques$', views.infoPratiques, name='info'),
    url(r'^transportEtAcces$', views.transportEtAcces,name='acces'),
    url(r'^logement$', views.logement,name='logement'),
    url(r'^nounou$', views.nounou,name='nounou'),
    url(r'^tpl$',views.tpl,name='tpl'),
    url(r'^accueil$',views.accueil,name='accueil'),
    url(r'^adresse$',views.adresse,name='adresse'),
    
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$',views.addition,name='calcul'),

   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


