from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff,
                     is_superuser, **extra_fields):
        # se normaliza y comprueba que se reciba un correro electronico
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')

        # Se crea un objeto con los datos recibidos por parametro
        user = self.model(username=username, email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser, **extra_fields)

        # Se realiza el proceso de hash del password o contraseña
        user.set_password(password)

        # Se garda el usuario en la base de datos utilizada actualmente
        user.save(using=self._db)

        # Se retorna el usuario creado
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True,
                                 True, **extra_fields)


# Modelo Usuario, utilizado por el modelo Cliente, el modelo comercio.
# Tambien utilizado como Administrador o superusuario.
class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    # Se especifica el Manager para el modelo de usuario
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Se especifica el campo a utilizar como Nombre de Usuario
    USERNAME_FIELD = 'username'
    # Se especifican los campos requeridos.
    REQUIRED_FIELDS = ['email']

    # Funcion que retorna el nombre de usuario, como nombre corto del objeto, al realizarse un llamado a este.
    def get_short_name(self):
        return self.username


class Especialidad(models.Model):
    nombre_esp = models.CharField(blank=False, max_length=50)
    descrip = models.TextField(verbose_name='Descripción de Especialidad')

    def __str__(self):
        return self.nombre_esp

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'


class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nombre de Medico')
    apellido = models.CharField(max_length=50, blank=False, null=False, verbose_name='Apellido de Medico')
    cedula = models.CharField(max_length=10, unique=True, blank=False, verbose_name='Identificación')
    direccion = models.TextField(max_length=100, verbose_name='Dirección', blank=False, null=False)
    telefono = models.CharField(max_length=10, verbose_name='Numero de Telefono')
    foto = models.FileField(upload_to='pacientes')
    masc = "Masculino"
    fem = "Femenino"
    choices_genero = (
        (masc, 'Masculino'), (fem, 'Femenino')
    )
    genero = models.CharField(blank=False, max_length=50, choices=choices_genero)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medico'


class Especialidad_Medico(models.Model):
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Nombre del Medico')
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE,
                                        verbose_name='Nombre de la Especialidad')

    Lunes = 'Lunes'
    Martes = 'Martes'
    Miercoles = 'Miercoles'
    Jueves = 'Jueves'
    Viernes = 'Viernes'

    Dias_Laborables = [
        (Lunes, 'Lunes'),
        (Martes, 'Martes'),
        (Miercoles, 'Miercoles'),
        (Jueves, 'Jueves'),
        (Viernes, 'Viernes'),
    ]

    dia_laboral = models.CharField(max_length=20, choices=Dias_Laborables, help_text='Seleccione un dia',
                                   verbose_name='Dia Laboral')

    horario_1 = '8:h00 - 8h30'
    horario_2 = '8h30 - 9h00'
    horario_3 = '9h00 - 10h00'
    horario_4 = '10h00 - 10h30'
    horario_5 = '10h30 - 11h00'
    horario_6 = '11h30 - 12h00'
    horario_7 = '12:h00 - 12h30'
    horario_8 = '12h30 - 13h00'
    horario_9 = '13h00 - 13h30'
    horario_10 = '13h30 - 14h00'
    horario_11 = '14h300 - 14h00'
    horario_12 = '14h00 - 14h30'
    horario_13 = '14:h30 - 15h00'
    horario_14 = '15h00 - 15h30'
    horario_15 = '15h30 - 16h00'
    horario_16 = '16h00 - 16h30'
    horario_17 = '16h30 - 17h00'
    horario_18 = '17h00 - 17h30'
    horario_19 = '17h30 - 18h00'

    Horarios_de_Atencion = [
        (horario_1, '8:h00 - 8h30'),
        (horario_2, '8h30 - 9h00'),
        (horario_3, '9h00 - 10h00'),
        (horario_4, '10h00 - 10h30'),
        (horario_5, '10h30 - 11h00'),
        (horario_6, '11h30 - 12h00'),
        (horario_7, '12:h00 - 12h30'),
        (horario_8, '12h30 - 13h00'),
        (horario_9, '13h00 - 13h30'),
        (horario_10, '13h30 - 14h00'),
        (horario_11, '14h300 - 14h00'),
        (horario_12, '14h00 - 14h30'),
        (horario_13, '14:h30 - 15h00'),
        (horario_14, '15h00 - 15h30'),
        (horario_15, '15h30 - 16h00'),
        (horario_16, '16h00 - 16h30'),
        (horario_17, '16h30 - 17h00'),
        (horario_18, '17h00 - 17h30'),
        (horario_19, '17h30 - 18h00'),
    ]

    horario = models.CharField(max_length=30, choices=Horarios_de_Atencion, help_text='Seleccione el horario',
                               verbose_name='Horario de Atención')

    def __str__(self):
        return "%s %s %s %s " % (self.id_medico, self.id_especialidad, self.dia_laboral, self.horario)

    class Meta:
        unique_together = ['id_medico', 'id_especialidad', 'dia_laboral', 'horario']


class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='usuarioP')
    nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nombre de Paciente')
    apellido = models.CharField(max_length=50, blank=False, null=False, verbose_name='Apellido de Paciente')
    cedula = models.CharField(max_length=10, unique=True, blank=False, verbose_name='Identificación')
    direccion = models.TextField(max_length=100, verbose_name='Dirección', blank=False, null=False)
    telefono = models.CharField(max_length=10, verbose_name='Numero de Telefono')
    foto = models.FileField(upload_to='pacientes')
    masc = "Masculino"
    fem = "Femenino"
    choices_genero = (
        (masc, 'Masculino'), (fem, 'Femenino')
    )
    genero = models.CharField(blank=False, max_length=50, choices=choices_genero)

    def __str__(self):
        return '%s %s - %s' % (self.nombre, self.apellido, self.cedula)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Cita(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    esp_medic = models.ForeignKey(Especialidad_Medico, on_delete=models.CASCADE, verbose_name='Disponibilidad')
    fecha_cita = models.DateField()

    Consulta = 'Consulta'
    RevisionExamenes = 'Revisión de Exámenes'
    Otro = 'Otro'

    motivo_choices = [
        (Consulta, 'Consulta'),
        (RevisionExamenes, 'Revisión de Exámenes'),
        (Otro, 'Otro'),
    ]

    motivo = models.CharField(max_length=20, verbose_name='Motivo de cita', choices=motivo_choices)

    def __str__(self):
        return "%s %s %s %s" % (self.paciente, self.esp_medic, self.fecha_cita, self.motivo)

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        unique_together = ['esp_medic', 'fecha_cita']


class Medicamento(models.Model):
    nombre = models.CharField(blank=False, max_length=50)
    presentacion = models.CharField(blank=False, max_length=50)
    volumen = models.CharField(blank=False, max_length=50)

    descripcion = models.TextField(blank=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.presentacion)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    diagnostico = models.TextField(blank=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.paciente, self.medico)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'


class Receta(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name='Medicamento')

    descripcion = models.CharField(max_length=200, blank=False, verbose_name='Indicación')

    class Meta:
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'

    def __str__(self):
        return '%s %s' % (self.medicamento, self.descripcion)


class Consultorio(models.Model):
    nombre = models.CharField(blank=False, max_length=50)
    direccion = models.TextField(blank=False)
    mision = models.TextField(blank=False)
    vision = models.TextField(blank=False)
    eslogan = models.CharField(blank=False, max_length=150)
    telefono = models.CharField(blank=False, max_length=50)
    correo = models.EmailField(blank=False)
    foto = models.ImageField(upload_to='home')


class Examen(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=False, verbose_name='Nombre del Examen')
    descrip = models.CharField(max_length=100, verbose_name='Descripción del Examen')

    def __str__(self):
        return self.nombre


class Historiaclinica(models.Model):
    id_cita = models.ForeignKey(Cita, on_delete=models.CASCADE, verbose_name='Cita')
    diagnostico = models.TextField( verbose_name='Diagnóstico')
    examen = models.ManyToManyField(Examen)
    receta = models.ManyToManyField(Receta)

    def __str__(self):
        return '%s %s %s' % (self.id_cita, self.examen, self.receta)

    def display_examen(self):
        return ', '.join([examen.nombre for examen in self.examen.all()])

    display_examen.short_description = 'Examen'

    def display_rece(self):
        return ', '.join([receta.medicamento.descripcion for receta in self.receta.all()])

    display_rece.short_description = 'Receta'
