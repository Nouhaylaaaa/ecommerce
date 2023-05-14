from django.shortcuts import render, get_object_or_404,redirect
from .models import Produit,Panier,Commandee
from .forms import ReglementForm
from datetime import date
# Create your views here.
def home1(request):
    search_query = request.GET.get('search', '')
    if search_query:
        produits = Produit.objects.filter(designation__icontains=search_query)
    else:
        produits = Produit.objects.all()
    return render(request, 'home1.html', {'produits': produits})
def produit_detail(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'produit_detail.html', {'produit': produit})

def panier(request):
    panier, created = Panier.objects.get_or_create(user=request.user)
    total = panier.get_total()  # Obtenez le total du panier en utilisant la méthode get_total()
    return render(request, 'panier.html', {'panier': panier, 'total': total})



def ajouter_panier(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    panier, created = Panier.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        for _ in range(quantity):
            commande = Commandee(produitP=produit, user=request.user)
            commande.save()
            panier.commande.add(commande)

    return redirect('panier')


def supprimer_panier(request, commande_id):
    commande = get_object_or_404(Commandee, id=commande_id)

    # Vérifier si la commande appartient à l'utilisateur actuel
    if commande.user == request.user:
        panier = Panier.objects.get(user=request.user)

        # Supprimer la commande du panier
        panier.commande.remove(commande)

        # Supprimer la commande de la base de données
        commande.delete()

    return redirect('panier')


def paiement(request):
    panier = Panier.objects.get(user=request.user)
    montant_total = panier.get_total()

    if request.method == 'POST':
        reglement_form = ReglementForm(request.POST)
        if reglement_form.is_valid():
            reglement = reglement_form.save(commit=False)
            reglement.montant = montant_total
            reglement.commandeC = panier.commande.first()
            reglement.save()
            panier.commande.clear()
            return redirect('confirmation_paiement')
    else:
        reglement_form = ReglementForm(initial={'montant': montant_total, 'date_reglement': date.today()})

    return render(request, 'paiement.html', {'reglement_form': reglement_form, 'panier': panier})



