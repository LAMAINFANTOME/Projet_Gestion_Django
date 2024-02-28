from django.contrib import admin
from .models import Annonce, Commentaire, Categorie
# Register your models here.

admin.site.register(Annonce)
admin.site.register(Commentaire)
admin.site.register(Categorie)
