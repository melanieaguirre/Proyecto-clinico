import json
from django.db.models.expressions import Random
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views import View

from .forms import RecetaForm
from .models import *
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class RecetaView(View):
    template_name = "atencion/receta/listar.html"

    def get(self, request, *args, **kwargs):
        data = {}
        action = request.GET.get("action")
        if action:
            if action == 'add':
                data['id_paciente'] = id_paciente = request.GET.get("id_paciente", "")
                data['title'] = 'Registrar Receta'
                data['form'] = RecetaForm
                data['frecuencia'] = Frecuencia.objects.filter(estado=True)
                data['duracion'] = Duracion.objects.filter(estado=True)
                data['medicamento'] = Medicamento.objects.filter(estado=True)
                data['dosis'] = Dosis.objects.filter(estado=True)
                return render(request, "atencion/receta/receta.html", data)
            elif action == 'ver':
                data['id_paciente'] = id_paciente = request.GET.get("id_paciente", "")
                data['id'] = id = request.GET.get("id", "")
                data['receta'] = receta = Receta.objects.get(pk=id)
                data['detalle'] = DetalleReceta.objects.filter(receta=receta).order_by('medicamento__descripcion')
                data['form'] = RecetaForm(instance=receta, ver=True)
                return render(request, "atencion/receta/receta_detalle.html", data)
        else:
            data['id_paciente'] = id_paciente = request.GET.get("id_paciente", "")
            paciente = Paciente.objects.get(pk=id_paciente)
            data['title'] = 'Receta'
            data['titulo'] = "Recetas de {}".format(paciente)
            data['listado'] = Receta.objects.filter(paciente_id=id_paciente,estado=True).order_by('-pk')
            return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':

                form = RecetaForm(request.POST)
                if form.is_valid():
                    form.instance.paciente_id = int(request.POST['id_paciente'])
                    form.save()

                medicamentos = json.loads(request.POST['medicamentos'])
                for m in medicamentos['items']:
                    detalle = DetalleReceta(receta=form.instance,medicamento_id=m['id'],cantidad=m['cantidad'],dosis_id=m['iddosis'],frecuencia_id=m['idfrecuencia'],duracion_id=m['idduracion'])
                    detalle.save()
                data["result"] = "ok"
                # form = self.form_class(request.POST)
                # form.save()

        except Exception as ex:
            data["error"] = str(ex)
        return JsonResponse(data, safe=False)
        # return HttpResponse(json.dumps(data), content_type="application/json")
