from django.db import models

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length = 150) 
    description = models.TextField()

# standards
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self) :
        return self.nom
    
class Annonce(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_post = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name="announce")
    autor = models.ForeignKey(User,on_delete=models.CASCADE,related_name="announce")
    status = models.BooleanField(default= False)
    def __str__(self) :
        return self.titre

class Commentaire(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='commentaires')
    autor = models.ForeignKey(User,on_delete=models.CASCADE,related_name="commentaires",default='homegnon')
    contenu = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.contenu