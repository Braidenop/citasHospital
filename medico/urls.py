from django.urls import path
from medico.views import *

app_name = 'medico'

urlpatterns = [
    path('', homeMedico.as_view(), name='home_medico'),
    path('registro', RegistroMedico.as_view(), name='registro_medico'),
    path('login', LoginMedico.as_view(), name='login_medico'),
    path('logout', LogoutView.as_view(), name='logout_medico'),
]