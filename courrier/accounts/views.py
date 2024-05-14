from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from .models import Signup, Login
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authentifier l'utilisateur
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Rediriger vers la page d'accueil ou une autre page après la connexion
                return redirect('index')
            else:
                # Gérer le cas où l'authentification a échoué
                return render(request, "accounts/login.html", {'form': form, 'error': 'E-mail ou mot de passe incorrect.'})
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            existing_users = User.objects.filter(username=email)
            if existing_users.exists():
                # Gérer le cas où l'utilisateur existe déjà
                return render(request, "accounts/signup.html", {'form': form, 'error': 'Un compte avec cet e-mail existe déjà.'})
            else:
                # Créer un nouvel utilisateur
                user = User.objects.create_user(username=email, password=password)
                # Enregistrement des autres champs personnalisés

                user.save()
            # Rediriger vers la page d'accueil ou une autre page après l'inscription
            return redirect('login')
    else:
        # Afficher le formulaire d'inscription vide
        form = SignupForm()

    return render(request, "accounts/signup.html", {'form': form})


