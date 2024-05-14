from django import forms

from Dashboard.models import Rappel, Courrier


class CourrierForm(forms.ModelForm):
    class Meta:
        model = Courrier
        fields = ['expediteur', 'destinataire', 'sujet', 'description', 'date', 'categorie', 'urgence', 'fichier']
        widgets = {
            'fichier': forms.FileInput(attrs= { 'required': 'required'}),
        }
   

class RappelForm(forms.ModelForm):
     date_rappel = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
     description = forms.CharField(max_length=255, widget=forms.Textarea())

     class Meta:
        model = Rappel
        fields = ['date_rappel', 'description']