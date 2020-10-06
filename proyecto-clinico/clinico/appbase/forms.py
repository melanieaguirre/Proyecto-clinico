from django import forms
from django.db.models import fields
from .models import *


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'consultorio': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'horario': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'duracion': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        widgets = {
            'dia': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'desde': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hasta': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class SignoVitalForm(forms.ModelForm):
    class Meta:
        model = SignoVital
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rango1': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rango2': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'medida': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'motivo': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
