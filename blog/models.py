from django.db import models
from django.utils import timezone
from datetime import datetime


class Guest(models.Model):
    nom = models.CharField(max_length=100)
    conjoint = models.CharField(max_length=100,blank=True)
    enfants = models.BooleanField()
    adresse = models.TextField(null=True)
    

    def publish(self):
        self.save()

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.nom

