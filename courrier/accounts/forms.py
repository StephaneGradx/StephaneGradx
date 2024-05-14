from django import forms


class SignupForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=128)
    prenom = forms.CharField(label="Prenom", max_length=128)
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe",  max_length=15)


class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe", max_length=15)
    

