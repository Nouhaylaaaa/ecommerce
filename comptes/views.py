from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
def create_user(request):
    if request.user.is_authenticated:
        return redirect('home1')
    else:
        form = CreateUserForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('connexion')
        return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.user.is_authenticated:
        return redirect('home1')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home1')
            else:
                messages.info(request, 'username or pwd is incorrect')
        context = {}
        return render(request, 'connexion.html', context)


@login_required(login_url='connexion')
def home(request):
    return render(request,'home1.html')

def logoutUser(request):
    logout(request)
    return redirect('connexion')



