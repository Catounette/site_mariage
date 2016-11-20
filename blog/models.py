from django.db import models
from django.utils import timezone
from datetime import datetime


class Guest(models.Model):
    nom = models.CharField(max_length=100)
    conjoint = models.CharField(max_length=100,blank=True)
    enfants = models.BooleanField()
    adresse = models.TextField(null=True)
    vientSure = models.BooleanField()
    vientPeut_etre = models.BooleanField()
    vientPas = models.BooleanField()
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.nom

