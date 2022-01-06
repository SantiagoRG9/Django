from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Category, Product


def myfirstview(request):
    data = {
        'name' : 'William',
        'categories' : Category.objects.all()
    }
    return render(request, 'home.html', data)


def mysecondview(request):
    data = {
        'name' : 'William',
        'products' : Product.objects.all()
    }
    return render(request, 'index2.html', data)
