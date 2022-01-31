from django.urls import path

from citas.views import *

app_name= 'citas'

urlpatterns = [

    path('', homePaciente.as_view(), name='homePaciente'),
    path('registro', Registro.as_view(), name='registro'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('lista_citas', AgendaCita.as_view(), name='lista_citas'),
    path('crear_cita', CrearCita.as_view(), name='crear_cita'),
    path('editar_cita/<int:pk>/', EditarCita.as_view(), name= 'editar_cita' ),
    path('eliminar_cita/<int:pk>/', EliminarCita.as_view(), name='eliminar_cita'),
]