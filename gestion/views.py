from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from .models import Annonce, Commentaire, Categorie


# Create your views here.

def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')


def productsingle (request,id):
    annonce = Annonce.objects.get(id=id)
    commentaires = Commentaire.objects.filter(annonce=annonce)
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('message')
        com = Commentaire()
        com.autor = user
        com.annonce = annonce
        com.contenu = message
        com.save()
        return redirect('product-single', id=annonce.id)

    datas={
        'annonce': annonce,
        'commentaires':commentaires
    }
    return render(request, 'product-single.html', datas)


def shop (request):
    annonces = Annonce.objects.filter(status='True')
    datas={
        'annonces':annonces
    }
    return render(request, 'shop.html', datas)

def contact (request):
    
    datas={

    }
    return render(request, 'contact.html', datas)


def cart (request):
    
    datas={

    }
    return render(request, 'cart.html', datas)


def blogsingle (request):
    
    datas={

    }
    return render(request, 'blog-single.html', datas)

def annonce (request):
    categories = Categorie.objects.all()
    user=request.user
    if request.method =='POST':
        titre = request.POST.get('titre')
        categorie = request.POST.get('categorie')
        prix = request.POST.get('prix')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        categorie_final = Categorie.objects.get(nom=categorie)
        announce = Annonce()
        announce.titre = titre
        announce.categorie = categorie_final
        announce.prix = prix
        announce.description = description
        announce.image = image
        announce.autor = user
        announce.save()
        return redirect('annonce')
    datas = {
        'categories': categories,
    }
    return render(request, 'annonce.html',datas)


def inscription(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpwd = request.POST['comfirmpwd']
        if User.objects.filter(username=username):
            messages.error(request, 'username already taken please try another.')
            return redirect('inscription')
        if User.objects.filter(email=email):
            messages.error(request, 'This email has an account.')
            return redirect('inscription')
        if not username.isalnum():
            User.error(request, 'username must be alphanumeric')
            return redirect('inscription')
        if password != confirmpwd:
            User.error(request, 'The password did not match! ')  
            return redirect('inscription')                  
        
        my_user = User.objects.create_user(username, email, password)
        my_user.first_name =firstname
        my_user.last_name = lastname 
        my_user.is_active = True
        my_user.save()
        
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            #### redirection si les infos sont correctes
            return redirect('index')
        
    return render(request, 'inscription.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            #### redirection si les infos sont correctes
            return redirect('index')
        else:
            print("login échoué")
           # message = "Merci de vérifiez vos informations"

    return render(request,"connexion.html")



