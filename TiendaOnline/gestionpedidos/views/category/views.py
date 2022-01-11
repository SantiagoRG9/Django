from os import name
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from gestionpedidos.models import Category
from gestionpedidos.forms import CategoryForm
from django.urls import reverse_lazy

def category_list(request):
    data = {
        'title' : 'Listado de categorias',
        'categories' : Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):

    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         return redirect('category_list2')
    #     return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        cat = Category.objects.get(pk=request.POST['id'])
        data['name'] = cat.names 
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorias'
        context['create_url'] = reverse_lazy('categoryCreate')
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('categoryList')

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
      
       
        # cat = Category.objects.get(pk=request.POST['id'])
        # data['name'] = cat.names 
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de una categoria'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('categoryList')
        context['create_url'] = reverse_lazy('categoryCreate')
        context['entity'] = 'Categorias'
        context['action'] = 'add'

        return context