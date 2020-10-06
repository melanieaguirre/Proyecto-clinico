from django.urls import path
from .views import PacienteView, CrearPacienteView, EditarPacienteView, EliminarPacienteView
from .doctor import *
from .horario import *
from .signosvitales import *
from .agenda import *

app_name = 'base'
urlpatterns = [
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('editar_paciente/<int:pk>/', EditarPacienteView.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/', EliminarPacienteView.as_view(), name='eliminar_paciente'),
    # DOCTOR
    path('doctor/', DoctorView.as_view(), name='doctor'),
    path('crear_doctor/', CrearDoctorView.as_view(), name='crear_doctor'),
    path('editar_doctor/<int:pk>/', EditarDoctorView.as_view(), name='editar_doctor'),
    path('eliminar_doctor/<int:pk>/', EliminarDoctorView.as_view(), name='eliminar_doctor'),
    # HORARIO
    path('horario/', HorarioView.as_view(), name='horario'),
    path('crear_horario/', CrearHorarioView.as_view(), name='crear_horario'),
    path('editar_horario/<int:pk>/', EditarHorarioView.as_view(), name='editar_horario'),
    path('eliminar_horario/<int:pk>/', EliminarHorarioView.as_view(), name='eliminar_horario'),
    # SIGNOS VITALES
    path('signos/', SignoVitalView.as_view(), name='signos'),
    path('crear_signos/', CrearSignoVitalView.as_view(), name='crear_signos'),
    path('editar_signos/<int:pk>/', EditarSignoVitalView.as_view(), name='editar_signos'),
    path('eliminar_signos/<int:pk>/', EliminarSignoVitalView.as_view(), name='eliminar_signos'),
    # CITAS
    path('citas/', AgendaView.as_view(), name='citas'),
    path('crear_citas/', CrearAgendaView.as_view(), name='crear_citas'),
    path('editar_citas/<int:pk>/', EditarAgendaView.as_view(), name='editar_citas'),
    path('eliminar_citas/<int:pk>/', EliminarAgendaView.as_view(), name='eliminar_citas'),
]
