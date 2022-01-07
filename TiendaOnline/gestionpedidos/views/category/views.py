from django.shortcuts import render

from gestionpedidos.models import Category


def category_list(request):
    data = {
        'title' : 'Listado de categorias',
        'categories' : Category.objects.all()
    }
    return render(request, 'category/list.html', data)
