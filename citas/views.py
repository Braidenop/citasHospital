from annoying.functions import get_object_or_None
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import LoginForm, FormularioLogin, AgendaCitaForm
from .models import Usuario, Paciente, Cita, Consulta, Especialidad_Medico
from .forms import LoginForm, RegistroUsuarioForm, RegistroPacienteForm
from django.contrib.auth import views as auth_views
from django import forms

# Create your views here.
"""
def Registro(request):
	return render(request, 'clinico/registro.html')
"""


class homePaciente(TemplateView):
    template_name = 'homePaciente.html'


class Registro(TemplateView):
    template_name = 'registro.html'

    def get_context_data(self, **kwargs):
        context = super(Registro, self).get_context_data(**kwargs)
        context['usuarioForm'] = RegistroUsuarioForm()
        context['pacienteForm'] = RegistroPacienteForm()
        return context

    def post(self, request, *args, **kwargs):
        usuario = RegistroUsuarioForm(request.POST)
        paciente = RegistroPacienteForm(request.POST, request.FILES)
        if usuario.is_valid() and paciente.is_valid():
            Usuario.objects.create_user(username=usuario.cleaned_data['username'],
                                        email=usuario.cleaned_data['email'],
                                        password=usuario.cleaned_data['password']
                                        )
            # Se crea un objeto Usuario con el Usuario recien guardado
            usuario = Usuario.objects.get(username=usuario.cleaned_data['username'])
            paciente = paciente.save(commit=False)
            paciente.usuario = usuario
            paciente.save()
            print(paciente)
            print(usuario)
            return redirect('citas:login')
        else:
            context = super(Registro, self).get_context_data(**kwargs)
            context['usuarioForm'] = usuario
            context['pacienteForm'] = paciente
            return render(request, 'registro.html', context)


# class Dashboard(LoginRequiredMixin, TemplateView):
#     login_url = 'clinico:login'
#
#     template_name = 'dashboard.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Dashboard, self).get_context_data(**kwargs)
#         context['paciente'] = Paciente.objects.get(usuario=self.request.user.id)
#         context['citas'] = Cita.objects.all().filter(paciente=context['paciente'])
#         context['consultas'] = Consulta.objects.all().filter(paciente=context['paciente'])
#         return context


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('citas:lista_citas')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def Logout(request):
    logout(request)
    return redirect('/')


# class SolicitudCita(TemplateView):
#     template_name = 'pacientes/cita.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(SolicitudCita, self).get_context_data(**kwargs)
#         context['paciente'] = Paciente.objects.get(usuario=self.request.user.id)
#         return context


class AgendaCita(ListView):
    model = Cita
    template_name = 'ListaCItas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Citas'
        context['create_url'] = reverse_lazy('citas:crear_cita')
        context['list_url'] = reverse_lazy('citas:lista_citas')
        context['entity'] = 'Listas'
        return context


class CrearCita(CreateView, LoginRequiredMixin):
    model = Cita
    template_name = 'crearCita.html'
    fields = ['esp_medic', 'fecha_cita', 'motivo']
    success_url = reverse_lazy('citas:lista_citas')
    url_redirect = success_url

    # def get_form_kwargs(self):
    #     kwargs = {'user' : self.request.user, }
    #     return kwargs

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Cita.objects.filter(paciente=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CrearCita, self).get_context_data(**kwargs)
        context['title'] = 'Agendamiento de Cita'
        context['entity'] = 'Citas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

    def form_valid(self, form):
        form.instance.paciente = self.request.user
        self.object = form.save
        return super(CrearCita, self).form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = AgendaCitaForm(request.POST)
    #     if form.is_valid():
    #         usuario = Paciente.objects.get(usuario_id=request.user.id)
    #         cita = form.save(commit=False)
    #         cita.usuario = usuario
    #         cita.save()
    #         print(cita)
    #         return redirect('citas:lista_citas')
    #
    #     else:
    #         context = super(CrearCita, self).get_context_data(**kwargs)
    #         context['agendarcitaForm'] = AgendaCitaForm()
    #
    #     return render(request, 'crearCita.html', context)


# def crearcita (request, cita_id):
#     cita = get_object_or_None(Cita, pk = cita_id)
#     if request.method == "POST":
#         usuario = Paciente.objects.get(usuario_id=request.user.id)
#         form =AgendaCitaForm(request.POST, instance=cita, paciente=usuario)
#         if form.is_valid():
#             cita = form.save()
#             return redirect('citas:lista_citas')
#     else:
#         usuario = Paciente.objects.get(usuario_id=request.user.id)
#         form = AgendaCitaForm(instance=cita, paciente=usuario)
#
#     context = {
#         'form':form,
#         'cita': cita
#     }
#
#     return render('crearCita.html', context)

class EditarCita(UpdateView, LoginRequiredMixin):
    model = Cita
    template_name = 'crearCita.html'
    fields = ['esp_medic', 'fecha_cita', 'motivo']
    success_url = reverse_lazy('citas:lista_citas')
    url_redirect = success_url

    # def get_form_kwargs(self):
    #     kwargs = {'user' : self.request.user, }
    #     return kwargs

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Cita.objects.filter(paciente=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(EditarCita, self).get_context_data(**kwargs)
        context['title'] = 'Agendamiento de Cita'
        context['entity'] = 'Citas'
        context['list_url'] = self.success_url
        context['action'] = 'change'
        return context

    def form_valid(self, form):
        form.instance.paciente = self.request.user
        self.object = form.save
        return super(EditarCita, self).form_valid(form)


class EliminarCita(DeleteView, LoginRequiredMixin):
    model = Cita
    template_name = 'eliminarCita.html'
    success_url = reverse_lazy('citas:lista_citas')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super(EliminarCita, self).get_context_data(**kwargs)
        context['title'] = 'Agendamiento de Cita'
        context['entity'] = 'Citas'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context


class LogoutView(auth_views.LogoutView):
    next_page = '/'
