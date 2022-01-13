from django import views
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista Produtos')


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe Produto')


class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar no Carrinho')


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove do Carrinho')


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
