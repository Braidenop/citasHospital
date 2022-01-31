from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Especialidad_Medico, Cita, Usuario


class EspecialidadAdmin(admin.ModelAdmin):
    model = Especialidad
    list_display = ('nombre_esp', 'descrip')


class MedicoAdmin(admin.ModelAdmin):
    model = Medico
    list_display = ('usuario', 'nombre', 'apellido', 'cedula', 'direccion',
                    'telefono', 'genero')
    search_fields = ('nomb', 'ident')


class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    list_display = ('usuario', 'nombre', 'apellido', 'cedula', 'direccion',
                    'telefono', 'genero',)


class Espcialidad_MedicoAdmin(admin.ModelAdmin):
    model = Especialidad_Medico
    list_display = ('id_medico', 'id_especialidad', 'dia_laboral', 'horario')


class CitAdmin(admin.ModelAdmin):
    model = Cita


admin.site.register(Usuario)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cita, CitAdmin)
admin.site.register(Especialidad_Medico, Espcialidad_MedicoAdmin)
