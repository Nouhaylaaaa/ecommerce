
from django.db import models

from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=128)
    def __str__(self):
        return self.nom_categorie

class Produit(models.Model):
    designation = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    prix = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="products",blank=True ,null=True)
    quantite = models.IntegerField(default=0)
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.designation



class Commandee(models.Model):
    date_cmd = models.DateField(default=date.today)
    ETAT_CHOICES = [
        ('ATT', 'En attente'),
        ('ENC', 'En cours de traitement'),
        ('TER', 'Terminé')
    ]
    etat_cmd = models.CharField(max_length=3,choices=ETAT_CHOICES,default='ATT')
    produitP = models.ForeignKey(Produit,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.etat_cmd

class Reglement(models.Model):
    num_carte = models.CharField(max_length=128)
    montant = models.FloatField()
    date_reglement = models.DateField(default=date.today)
    commandeC = models.ForeignKey(Commandee, on_delete= models.CASCADE)
    def __str__(self):
        return self.montant

class Panier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    commande = models.ManyToManyField(Commandee)

    def __str__(self):
        return self.user


