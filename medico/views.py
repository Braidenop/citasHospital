from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from medico.forms import RegistroMedicoForm, RegistroUsuarioForm, FormularioLogin, HistoriaForm
from citas.models import Usuario, Medico, Cita, Paciente, Especialidad_Medico, Historiaclinica
from django.contrib.auth import views as auth_views

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class homeMedico(TemplateView):
    template_name = 'medico/homeMedico.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['entity'] = Medico.objects.filter(usuario=self.request.user)
    #     return context


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


class ListaCita(ListView):
    model = Cita
    template_name = 'medico/lista_citas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Citas'
        context['entity'] = 'Listas Citas'
        return context

    def get_queryset(self):
        queryset = Cita.objects.select_related().filter(esp_medic__id_medico__usuario=self.request.user)
        return queryset


#Historia Clínica

# Cita

class HistoriaList(ListView):
    model = Historiaclinica
    template_name = 'medico/listhistoriaclinica.html'
    permission_required = 'view_historiaclinica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historias Clínicas'
        context['create_url'] = reverse_lazy('medico:crear_hist')
        context['list_url'] = reverse_lazy('medico:lista_hist')
        context['entity'] = 'Listas'
        return context


class HistoriaCrear(CreateView, LoginRequiredMixin):
    model = Historiaclinica
    template_name = 'medico/crear_historia.html'
    form_class = HistoriaForm
    success_url = reverse_lazy('medico:lista_hist')
    url_redirect = success_url
    permission_required = 'add_historiaclinica'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Historia Clinica'
        context['list_url'] = reverse_lazy('medico:lista_hist')
        context['action'] = 'add'
        return context


class EditarHist(UpdateView, LoginRequiredMixin):
    model = Historiaclinica
    template_name = 'medico/crear_historia.html'
    fields = ['id_cita', 'diagnostico', 'examen', 'receta']
    success_url = reverse_lazy('medico:lista_hist')
    url_redirect = success_url
    permission_required = 'change_historiaclinica'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditarHist, self).get_context_data(**kwargs)
        context['title'] = 'Edición de Historia Clinica'
        context['list_url'] = reverse_lazy('medico:lista_hist')
        context['action'] = 'edit'
        return context


class EliminarHist(DeleteView, LoginRequiredMixin):
    model = Historiaclinica
    template_name = 'medico/deletehist.html'
    success_url = reverse_lazy('medico:lista_hist')
    url_redirect = success_url
    permission_required = 'delete_historiaclinica'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EliminarHist, self).get_context_data(**kwargs)
        context['title'] = 'Eliminación de Historia Clínica'
        context['list_url'] = reverse_lazy('medico:lista_hist')
        context['action'] = 'delete'
        return context


class RecetaPDF(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('medico/receta_pdf.html')
            context = {
                'hist': Historiaclinica.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'Hospital Básico del Oro', 'ruc': '0999999999998', 'address':'El Oro'}
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('medico:lista_hist'))