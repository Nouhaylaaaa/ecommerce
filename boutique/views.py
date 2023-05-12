from django.shortcuts import render, get_object_or_404
from .models import Produit

# Create your views here.
def home1(request):
    produits = Produit.objects.all()
    return render(request,'home1.html',context={"produits":produits})
def produit_detail(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'produit_detail.html', {'produit': produit})
def panier(request):
    return render(request,'panier.html')


