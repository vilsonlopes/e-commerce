from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


# Create your views here.


class CriarPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Criar Perfil')


class UpdatePerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update Perfil')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
