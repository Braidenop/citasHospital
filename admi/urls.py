from django.urls import path
from admi.views import *

app_name = 'admi'

urlpatterns = [
    # Usuario
    path('', homeAdmin.as_view(), name='home'),
    path('list_usuarios/', listUsuarios.as_view(), name='lista_usuarios'),
    path('creación_usuario/', crearUsuario.as_view(), name='crear_usuario'),
    path('editar_usuario/<int:pk>/', editarUsuario.as_view(), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', eliminarUsuario.as_view(), name='eliminar_usuario'),

    # Especialidad
    path('list_espe/', listEspe.as_view(), name='lista_espe'),
    path('creación_espe/', crearEspe.as_view(), name='crear_espe'),
    path('editar_espe/<int:pk>/', editarEspe.as_view(), name='editar_espe'),
    path('eliminar_espe/<int:pk>/', eliminarEspe.as_view(), name='eliminar_espe'),

    # Medicos
    path('list_medi/', listMedi.as_view(), name='lista_medi'),
    path('creación_medi/', crearMedi.as_view(), name='crear_medi'),
    path('editar_medi/<int:pk>/', editarMedi.as_view(), name='editar_medi'),
    path('eliminar_medi/<int:pk>/', eliminarMedi.as_view(), name='eliminar_medi'),

]
