from django.contrib import admin
from boutique.models import Categorie, Produit, Commandee, Reglement, Panier

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Commandee)
admin.site.register(Reglement)
admin.site.register(Panier)
