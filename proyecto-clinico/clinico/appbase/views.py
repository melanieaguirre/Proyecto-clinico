from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm


# Vista de Inicio


class InicioView(TemplateView):
    template_name = "index.html"


# Vista de Pacientes
#    Lista los registros de los pacientes


class PacienteView(ListView):
    model = Paciente
    template_name = "base/paciente/paciente.html"
    context_object_name = "pacientes"
    queryset = Paciente.objects.filter(estado=False)
    paginate_by = 15

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context


#    Crea un nuevo registro de los pacientes


class CrearPacienteView(CreateView):
    model = Paciente
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


#    Edita o modifica  un registro de los pacientes


class EditarPacienteView(UpdateView):
    model = Paciente
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


class EliminarPacienteView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        paciente = Paciente.objects.get(id=pk)
        paciente.estado = False
        paciente.save()
        # object.estado = False
        # object.save()
        return redirect('base:paciente')
