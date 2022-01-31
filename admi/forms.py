from django import forms
from citas.models import Usuario, Especialidad, Medico
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
        fields = ['usuario', 'nombre','apellido' ,'cedula','direccion','foto','genero','telefono' ]
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
