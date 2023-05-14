from django.urls import path
from .views import home1,produit_detail,panier,ajouter_panier,supprimer_panier,paiement,Contact,AboutUs
urlpatterns = [
    path('',home1,name='home1'),
    path('produits/<int:produit_id>/', produit_detail, name='produit_detail'),
    path('panier/', panier, name='panier'),
    path('ajouter_panier/<int:produit_id>/', ajouter_panier, name='ajouter_panier'),
    path('supprimer_panier/<int:commande_id>/', supprimer_panier, name='supprimer_panier'),
    path('paiement/', paiement, name='paiement'),
    path('AboutUs/', AboutUs, name='AboutUs'),
    path('ContactPage/', Contact, name='ContactPage'),



]