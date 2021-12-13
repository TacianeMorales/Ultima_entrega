from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.base import TemplateView

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,

)
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from produtos.models import Category, Infos
# Create your views here.

class index(ListView):
    model = Category
    template_name = 'home.html'

@login_required
def ola(request):
    return HttpResponse('Olá, Django! Site do Vini')

def teste(request):
    return HttpResponse('Olá, deu certo')


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ('name', 'description')
    template_name = 'create_category.html'
    success_url = reverse_lazy('list_category')


class ListCategoryView(ListView):
    model = Category
    template_name = 'list_category.html'
    context_object_name = 'categories'

class DetailCategoryView(DetailView):
    model = Category
    template_name = 'category_detail.html'

class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'category_form.html'
    fields = ('name', 'description')
    sucecess_url = reverse_lazy('list_category')

class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    sucecess_url = reverse_lazy('list_category')

class CreatInfosProdutView(LoginRequiredMixin, CreateView):
    model = Infos
    fields = ('Produtname', 'ProdutPeso', 'ProdutMarca', 'ProdutUso')
    template_name = 'CreatInfosProdut.html'
    succes_url = reverse_lazy('ListInfosProdut/')

class ListInfosProdutView(ListView):
    model = Infos
    template_name = 'ListInfoProdut.html'
    context_object_name = 'informacoes'