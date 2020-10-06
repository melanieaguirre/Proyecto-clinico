from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class SignoVitalView(ListView):
    model = SignoVital
    template_name = "base/signos/listar.html"
    context_object_name = "listado"
    queryset = SignoVital.objects.filter(estado=False)
    paginate_by = 15

    def get_queryset(self):
        descripcion = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descripcion'] = self.request.GET.get('descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Signos Vitales"
        return context


class CrearSignoVitalView(CreateView):
    model = SignoVital
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/signos/form.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:signos')
    context_object_name = "signos"


class EditarSignoVitalView(UpdateView):
    model = SignoVital
    # fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/signos/form.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:signos')
    context_object_name = "signos"


class EliminarSignoVitalView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        filtro = SignoVital.objects.get(id=pk)
        filtro.estado = False
        filtro.save()
        return redirect('base:signos')
