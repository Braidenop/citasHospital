from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Usuario, Paciente, Cita


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'required': 'True'}))
    password = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'type': 'password', 'required': 'True'}))


class RegistroUsuarioForm(forms.ModelForm):
    passwordCheck = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': '',

               'required': 'True',
               'type': 'password'
               }))

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs=
            {
                'class': '',
            }),
            'email': forms.TextInput(attrs=
            {
                'type': 'email',
                'class': '',
            }),
            'password': forms.TextInput(attrs=
            {
                'type': 'password',
                'class': '',
                'required': 'True'
            })
        }

    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.data.get('passwordCheck')
        print(password2)

        if not password2:
            raise forms.ValidationError("Debes verificar tu contraseña.")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2


class RegistroPacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ('usuario',)
        widgets = {
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'cedula': forms.TextInput(),
            'direccion': forms.TextInput(attrs={'class': 'materialize-textarea'}),
            'foto': forms.FileInput(attrs={'class': ''}),
            'genero': forms.Select(attrs={'class': 'browser-default'}),
            'telefono': forms.TextInput(),

        }


class AgendaCitaForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user')
    #     self.paciente = user
    #     super(AgendaCitaForm, self).__init__(*args, **kwargs)



    class Meta:
        model = Cita
        fields = ['esp_medic', 'fecha_cita', 'motivo']
        widgets = {
            'esp_medic': forms.Select(),
            'fecha_cita': forms.DateInput(),

            'motivo': forms.Select(),

        }

    # def save(self, *args, **kwargs):
    #     self.instance.paciente = self.paciente
    #     cita = super(AgendaCitaForm, self).save(*args,**kwargs)
    #     return cita

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
