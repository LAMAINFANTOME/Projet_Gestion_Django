"""projet1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from gestion import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('inscription/',views.inscription,name='inscription'),
    path('connexion/',views.connexion,name='connexion'),
    path('product-single/<int:id>',views.productsingle,name='product-single'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('blog-single/',views.blogsingle,name='blogsingle'),
    path('annonce/',views.annonce,name='annonce'),
]