from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Courrier(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courriers_envoyes')
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courriers_recus')
    sujet = models.TextField()
    description = models.CharField(max_length=255)
    fichier = models.FileField(upload_to="C:/Users/Stephane/Documents/GESTION DU COURRIER/courrier/media")
    date = models.DateField()
    urgence = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)

class Rappel(models.Model):
    createur = models.ForeignKey(User, on_delete=models.CASCADE)
    courrier = models.ForeignKey(Courrier, on_delete=models.CASCADE)
    date_rappel = models.DateField()
    description = models.CharField(max_length=255)