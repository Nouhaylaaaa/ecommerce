from django.urls import path
from .views import home1,produit_detail,panier
urlpatterns = [
    path('home1/',home1,name='home1'),
    path('produits/<int:produit_id>/', produit_detail, name='produit_detail'),
    path('panier/', panier, name='panier'),



]