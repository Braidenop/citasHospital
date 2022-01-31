from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from citas.models import Usuario, Especialidad, Medico
from .forms import CrearUsuarioForm, UserCreationForm, EspecialidadForm, MedicoForm


class homeAdmin(TemplateView):
    template_name = 'admi/homeAdmi.html'


# Usuario
class listUsuarios(ListView, LoginRequiredMixin):
    model = Usuario
    template_name = 'admi/user/list_usuarios.html'
    permission_required = 'view_usuario'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['create_url'] = reverse_lazy('admi:crear_usuario')
        context['list_url'] = reverse_lazy('admi:lista_usuarios')
        context['entity'] = 'Usuarios'
        return context


class crearUsuario(LoginRequiredMixin, CreateView):
    model = Usuario
    template_name = 'admi/user/crear_usuario.html'
    form_class = CrearUsuarioForm
    success_url = reverse_lazy('admi:lista_usuarios')
    permission_required = 'add_usuario'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('admi:lista_usuarios')
        context['action'] = 'add'
        return context


class editarUsuario(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'admi/user/crear_usuario.html'
    form_class = CrearUsuarioForm
    success_url = reverse_lazy('admi:lista_usuarios')
    permission_required = 'change_usuario'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('admi:lista_usuarios')
        context['action'] = 'edit'
        return context


class eliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'admi/user/delete_user.html'
    success_url = reverse_lazy('admi:lista_usuarios')
    permission_required = 'delete_usuario'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('admi:lista_usuarios')
        context['action'] = 'delete'
        return context


# Especialidad

class listEspe(ListView, LoginRequiredMixin):
    model = Especialidad
    template_name = 'admi/especialidad/lista_espe.html'
    permission_required = 'view_especialidad'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Especialidades'
        context['create_url'] = reverse_lazy('admi:crear_espe')
        context['list_url'] = reverse_lazy('admi:lista_espe')
        context['entity'] = 'Especialidades'
        return context


class crearEspe(LoginRequiredMixin, CreateView):
    model = Especialidad
    template_name = 'admi/especialidad/crear_especialidad.html'
    form_class = EspecialidadForm
    success_url = reverse_lazy('admi:lista_espe')
    permission_required = 'add_especialidad'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Especialidad'
        context['entity'] = 'Especialidades'
        context['list_url'] = reverse_lazy('admi:lista_espe')
        context['action'] = 'add'
        return context


class editarEspe(LoginRequiredMixin, UpdateView):
    model = Especialidad
    template_name = 'admi/especialidad/crear_especialidad.html'
    form_class = EspecialidadForm
    success_url = reverse_lazy('admi:lista_espe')
    permission_required = 'change_especialidad'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Especialidad'
        context['entity'] = 'Especialidades'
        context['list_url'] = reverse_lazy('admi:lista_espe')
        context['action'] = 'edit'
        return context


class eliminarEspe(LoginRequiredMixin, DeleteView):
    model = Especialidad
    template_name = 'admi/especialidad/delete_espe.html'
    success_url = reverse_lazy('admi:lista_espe')
    permission_required = 'delete_especialidad'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Especialidad'
        context['entity'] = 'Especialidades'
        context['list_url'] = reverse_lazy('admi:lista_espe')
        context['action'] = 'delete'
        return context


# Medicos

class listMedi(ListView, LoginRequiredMixin):
    model = Medico
    template_name = 'admi/medico/list_medicos.html'
    permission_required = 'view_medico'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Médicos'
        context['create_url'] = reverse_lazy('admi:crear_medi')
        context['list_url'] = reverse_lazy('admi:lista_medi')
        context['entity'] = 'Medicos'
        return context


class crearMedi(LoginRequiredMixin, CreateView):
    model = Medico
    template_name = 'admi/medico/crear_medico.html'
    form_class = MedicoForm
    success_url = reverse_lazy('admi:lista_medi')
    permission_required = 'add_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Datos Personales del Médico'
        context['entity'] = 'Medicos'
        context['list_url'] = reverse_lazy('admi:lista_medi')
        context['action'] = 'add'
        return context


class editarMedi(LoginRequiredMixin, UpdateView):
    model = Medico
    template_name = 'admi/medico/crear_medico.html'
    form_class = MedicoForm
    success_url = reverse_lazy('admi:lista_espe')
    permission_required = 'change_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de datos de Medico'
        context['entity'] = 'Medicos'
        context['list_url'] = reverse_lazy('admi:lista_espe')
        context['action'] = 'edit'
        return context


class eliminarMedi(LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = 'admi/medico/delete_medico.html'
    success_url = reverse_lazy('admi:lista_espe')
    permission_required = 'delete_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Medico'
        context['entity'] = 'Medicos'
        context['list_url'] = reverse_lazy('admi:lista_espe')
        context['action'] = 'delete'
        return context
