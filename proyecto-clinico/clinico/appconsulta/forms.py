from django import forms
from django.db.models import fields
from .models import *


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        exclude = ['paciente', 'estado']

    def __init__(self, *args, **kwargs):
        ver = kwargs.pop('ver') if 'ver' in kwargs else False
        super(RecetaForm, self).__init__(*args, **kwargs)
        self.fields['sintoma'].queryset = Sintoma.objects.filter(estado=True)
        self.fields['diagnostico'].queryset = Diagnostico.objects.filter(estado=True)
        self.fields['gabinete'].queryset = EstudioGabinete.objects.filter(estado=True)
        for k, v in self.fields.items():
            self.fields[k].widget.attrs['class'] = "form-control"
            if k in ('sintoma','diagnostico','gabinete'):
                self.fields[k].widget.attrs['class'] = "form-control select2"
            self.fields[k].widget.attrs['required'] = "true"

            if ver:
                self.fields[k].widget.attrs['readonly'] = 'readonly'
                self.fields[k].widget.attrs['disabled'] = 'disabled'
