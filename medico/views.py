from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, FormView
from medico.forms import RegistroMedicoForm, RegistroUsuarioForm, FormularioLogin
from citas.models import Usuario, Medico
from django.contrib.auth import views as auth_views


class homeMedico(TemplateView):
    template_name = 'medico/homeMedico.html'


class RegistroMedico(TemplateView):
    template_name = 'medico/registroMedi.html'

    def get_context_data(self, **kwargs):
        context = super(RegistroMedico, self).get_context_data(**kwargs)
        context['usuarioForm'] = RegistroUsuarioForm()
        context['medicoForm'] = RegistroMedicoForm()
        return context

    def post(self, request, *args, **kwargs):
        usuario = RegistroUsuarioForm(request.POST)
        medico = RegistroMedicoForm(request.POST, request.FILES)
        if usuario.is_valid() and medico.is_valid():
            Usuario.objects.create_user(username=usuario.cleaned_data['username'],
                                        email=usuario.cleaned_data['email'],
                                        password=usuario.cleaned_data['password']
                                        )
            # Se crea un objeto Usuario con el Usuario recien guardado
            usuario = Usuario.objects.get(username=usuario.cleaned_data['username'])
            medico = medico.save(commit=False)
            medico.usuario = usuario
            medico.save()
            print(medico)
            print(usuario)
            return redirect('medico:login_medico')
        else:
            context = super(RegistroMedico, self).get_context_data(**kwargs)
            context['usuarioForm'] = usuario
            context['medicoForm'] = medico
            return render(request, 'medico/registroMedi.html', context)


class LoginMedico(FormView):
    template_name = 'medico/loginMedico.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('medico:home_medico')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginMedico, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginMedico, self).form_valid(form)


class LogoutView(auth_views.LogoutView):
    next_page = '/'
