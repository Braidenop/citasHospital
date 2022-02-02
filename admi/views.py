from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from citas.models import Usuario, Especialidad, Medico, Especialidad_Medico, Cita, Examen, Receta, Medicamento
from .forms import CrearUsuarioForm, UserCreationForm, EspecialidadForm, MedicoForm, DisponibilidadForm, CitaForm, \
    MedicamentoForm, ExamenForm, RecetaForm


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
    success_url = reverse_lazy('admi:lista_medi')
    permission_required = 'change_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de datos de Medico'
        context['entity'] = 'Medicos'
        context['list_url'] = reverse_lazy('admi:lista_medi')
        context['action'] = 'edit'
        return context


class eliminarMedi(LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = 'admi/medico/delete_medico.html'
    success_url = reverse_lazy('admi:lista_medi')
    permission_required = 'delete_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Medico'
        context['entity'] = 'Medicos'
        context['list_url'] = reverse_lazy('admi:lista_medi')
        context['action'] = 'delete'
        return context


# Disponibilidad

class listDispo(ListView, LoginRequiredMixin):
    model = Especialidad_Medico
    template_name = 'admi/disponiblidad/list_dispo.html'
    permission_required = 'view_especialidad_medico'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Disponibilidad de Horario'
        context['create_url'] = reverse_lazy('admi:crear_dipo')
        context['list_url'] = reverse_lazy('admi:lista_dipo')
        context['entity'] = 'Disponibilidad'
        return context


class crearDispo(LoginRequiredMixin, CreateView):
    model = Especialidad_Medico
    template_name = 'admi/disponiblidad/crear_dispo.html'
    form_class = DisponibilidadForm
    success_url = reverse_lazy('admi:lista_dipo')
    permission_required = 'add_especialidad_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Escoja la disponibilidad de Horario'
        context['entity'] = 'Disponibilidad'
        context['list_url'] = reverse_lazy('admi:lista_dipo')
        context['action'] = 'add'
        return context


class editarDispo(LoginRequiredMixin, UpdateView):
    model = Especialidad_Medico
    template_name = 'admi/disponiblidad/crear_dispo.html'
    form_class = MedicoForm
    success_url = reverse_lazy('admi:lista_dipo')
    permission_required = 'change_especialidad_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de datos de la disponibilidad de Horario'
        context['entity'] = 'Disponibilidad'
        context['list_url'] = reverse_lazy('admi:lista_dipo')
        context['action'] = 'edit'
        return context


class eliminarDispo(LoginRequiredMixin, DeleteView):
    model = Especialidad_Medico
    template_name = 'admi/disponiblidad/delete_dispo.html'
    success_url = reverse_lazy('admi:lista_dipo')
    permission_required = 'delete_especialidad_medico'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Horario'
        context['entity'] = 'Disponibilidad'
        context['list_url'] = reverse_lazy('admi:lista_dipo')
        context['action'] = 'delete'
        return context


# Cita

class AgendaCita(ListView):
    model = Cita
    template_name = 'admi/cita/list_cita.html'
    permission_required = 'view_cita'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Citas'
        context['create_url'] = reverse_lazy('admi:crear_cita')
        context['list_url'] = reverse_lazy('admi:lista_cita')
        context['entity'] = 'Listas'
        return context


class CrearCita(CreateView, LoginRequiredMixin):
    model = Cita
    template_name = 'admi/cita/crear_cita.html'
    form_class = CitaForm
    success_url = reverse_lazy('admi:lista_cita')
    url_redirect = success_url
    permission_required = 'add_cita'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CrearCita, self).get_context_data(**kwargs)
        context['title'] = 'Agendamiento de Cita'
        context['entity'] = 'Citas'
        context['list_url'] = reverse_lazy('admi:lista_cita')
        context['action'] = 'add'
        return context


class EditarCita(UpdateView, LoginRequiredMixin):
    model = Cita
    template_name = 'admi/cita/crear_cita.html'
    form_class = CitaForm
    success_url = reverse_lazy('citas:lista_citas')
    url_redirect = success_url
    permission_required = 'change_cita'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditarCita, self).get_context_data(**kwargs)
        context['title'] = 'Cambio de Cita'
        context['entity'] = 'Citas'
        context['list_url'] = reverse_lazy('admi:lista_cita')
        context['action'] = 'change'
        return context


class EliminarCita(DeleteView, LoginRequiredMixin):
    model = Cita
    template_name = 'admi/cita/delete_cita.html'
    success_url = reverse_lazy('admi:lista_cita')
    url_redirect = success_url
    permission_required = 'delete_cita'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EliminarCita, self).get_context_data(**kwargs)
        context['title'] = 'Eliminación de Cita'
        context['entity'] = 'Citas'
        context['list_url'] = reverse_lazy('admi:lista_cita')
        context['action'] = 'delete'
        return context


# Examenes

class listExamen(ListView, LoginRequiredMixin):
    model = Examen
    template_name = 'admi/examen/list_examenes.html'
    permission_required = 'view_examen'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Examenes'
        context['create_url'] = reverse_lazy('admi:crear_dipo')
        context['list_url'] = reverse_lazy('admi:lista_dipo')
        context['entity'] = 'Examen'
        return context


class crearExamen(LoginRequiredMixin, CreateView):
    model = Examen
    template_name = 'admi/examen/crear_examen.html'
    form_class = ExamenForm
    success_url = reverse_lazy('admi:lista_exa')
    permission_required = 'add_examen'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Un Examen '
        context['entity'] = 'Examen'
        context['list_url'] = reverse_lazy('admi:lista_exa')
        context['action'] = 'add'
        return context


class editarExamen(LoginRequiredMixin, UpdateView):
    model = Examen
    template_name = 'admi/examen/crear_examen.html'
    form_class = ExamenForm
    success_url = reverse_lazy('admi:lista_exa')
    permission_required = 'change_examen'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Un Examen '
        context['entity'] = 'Examen'
        context['list_url'] = reverse_lazy('admi:lista_exa')
        context['action'] = 'edit'
        return context


class eliminarExamen(LoginRequiredMixin, DeleteView):
    model = Examen
    template_name = 'admi/examen/delete_examen.html'
    success_url = reverse_lazy('admi:lista_exa')
    permission_required = 'delete_examen'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Examen'
        context['entity'] = 'Examen'
        context['list_url'] = reverse_lazy('admi:lista_exa')
        context['action'] = 'delete'
        return context


# Medicamento

class listMedicamento(ListView, LoginRequiredMixin):
    model = Medicamento
    template_name = 'admi/medicamento/list_medicamento.html'
    permission_required = 'view_medicamento'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Medicamentos'
        context['create_url'] = reverse_lazy('admi:crear_medica')
        context['list_url'] = reverse_lazy('admi:lista_medica')
        context['entity'] = 'Medicamento'
        return context


class crearMedicamento(LoginRequiredMixin, CreateView):
    model = Medicamento
    template_name = 'admi/medicamento/crear_medicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('admi:lista_medica')
    permission_required = 'add_medicamento'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Un Medicamento '
        context['entity'] = 'Medicamento'
        context['list_url'] = reverse_lazy('admi:lista_medica')
        context['action'] = 'add'
        return context


class editarMedicamento(LoginRequiredMixin, UpdateView):
    model = Medicamento
    template_name = 'admi/medicamento/crear_medicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('admi:lista_medica')
    permission_required = 'change_medicamento'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Un Medicamento '
        context['entity'] = 'Medicamento'
        context['list_url'] = reverse_lazy('admi:lista_medica')
        context['action'] = 'edit'
        return context


class eliminarMedicamento(LoginRequiredMixin, DeleteView):
    model = Medicamento
    template_name = 'admi/medicamento/delete_medi.html'
    success_url = reverse_lazy('admi:lista_medica')
    permission_required = 'delete_medicamento'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Medicamento'
        context['entity'] = 'Examen'
        context['list_url'] = reverse_lazy('admi:lista_medica')
        context['action'] = 'delete'
        return context


# Receta

class listReceta(ListView, LoginRequiredMixin):
    model = Receta
    template_name = 'admi/receta/list_receta.html'
    permission_required = 'view_receta'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Recetas'
        context['create_url'] = reverse_lazy('admi:crear_receta')
        context['list_url'] = reverse_lazy('admi:lista_receta')
        context['entity'] = 'Receta'
        return context


class crearReceta(LoginRequiredMixin, CreateView):
    model = Receta
    template_name = 'admi/receta/crear_receta.html'
    form_class = RecetaForm
    success_url = reverse_lazy('admi:lista_receta')
    permission_required = 'add_receta'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una receta  '
        context['entity'] = 'Receta'
        context['list_url'] = reverse_lazy('admi:lista_receta')
        context['action'] = 'add'
        return context


class editarReceta(LoginRequiredMixin, UpdateView):
    model = Receta
    template_name = 'admi/receta/crear_receta.html'
    form_class = RecetaForm
    success_url = reverse_lazy('admi:lista_receta')
    permission_required = 'change_receta'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una receta  '
        context['entity'] = 'Receta'
        context['list_url'] = reverse_lazy('admi:lista_receta')
        context['action'] = 'edit'
        return context


class eliminarReceta(LoginRequiredMixin, DeleteView):
    model = Receta
    template_name = 'admi/receta/delete_receta.html'
    success_url = reverse_lazy('admi:lista_receta')
    permission_required = 'delete_receta'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Receta'
        context['entity'] = 'Receta'
        context['list_url'] = reverse_lazy('admi:lista_medica')
        context['action'] = 'delete'
        return context
