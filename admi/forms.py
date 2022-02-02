from django import forms
from django.forms import DateTimeInput, DateInput

from citas.models import Usuario, Especialidad, Medico, Especialidad_Medico, Cita, Examen, Medicamento, Receta
from django.contrib.auth.forms import UserCreationForm


class CrearUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ["username", "email", "password1", "password2"]


class EspecialidadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_esp'].widget.attrs['autofocus'] = True

    class Meta:
        model = Especialidad
        fields = '__all__'
        widgets = {
            'nombre_esp': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese una Especialidad ',
                }
            ),
            'descrip': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese la Descripción',

                }
            ),
        }


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['usuario', 'nombre', 'apellido', 'cedula', 'direccion', 'foto', 'genero', 'telefono']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'browser-default'}),
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'cedula': forms.TextInput(),
            'direccion': forms.TextInput(attrs={'class': 'materialize-textarea'}),
            'foto': forms.FileInput(attrs={'class': ''}),
            'genero': forms.Select(attrs={'class': 'browser-default'}),
            'telefono': forms.TextInput(),

        }


class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad_Medico
        fields = ['id_medico', 'id_especialidad', 'dia_laboral', 'horario']
        widgets = {
            'id_medico': forms.Select(attrs={'class': 'browser-default'}),
            'id_especialidad': forms.Select(attrs={'class': 'browser-default'}),
            'dia_laboral': forms.Select(attrs={'class': 'browser-default'}),
            'horario': forms.Select(attrs={'class': 'browser-default'}),

        }


class DateImput(DateInput):
    input_type = 'date'


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'esp_medic', 'fecha_cita', 'motivo']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'browser-default'}),
            'esp_medic': forms.Select(attrs={'class': 'browser-default'}),
            'fecha_cita': DateImput(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'browser-default'}),
        }


class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['nombre', 'descrip']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'descrip': forms.Textarea(attrs={'placeholder': 'Ingrese una Descripción'}),
        }


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'presentacion', 'volumen']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'presentacion': forms.TextInput(attrs={'placeholder': 'Ingrese una Presentación'}),
            'volumen': forms.TextInput(attrs={'placeholder': 'Ingrese un Volumen'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Ingrese una Descripción'}),
        }


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['medicamento', 'descripcion']
        widgets = {
            'medicamento': forms.Select(attrs={'class': 'browser-default'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingrese la indicación'}),
        }
