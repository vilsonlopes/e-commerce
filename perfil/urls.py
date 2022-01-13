from django.urls import path
from . import views


app_name = 'perfil'

urlpatterns = [
    path('', views.CriarPerfil.as_view(), name='criarperfil'),
    path('update/', views.UpdatePerfil.as_view(), name='updateperfil'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
