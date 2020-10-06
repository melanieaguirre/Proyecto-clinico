import json
from django.db.models.expressions import Random
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views import View
from .models import *
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class HistoriaView2(View):
    template_name = "atencion/historia/historia2.html"

    def get(self, request, *args, **kwargs):
        data = {}
        action = request.GET.get("action")
        if action:
            if action == "data_antecedente":
                id_grupo_antecedente = request.GET.get("id_grupo_antecedente")
                grupo_antecedente = GrupoAntecedente.objects.get(
                    pk=int(id_grupo_antecedente))
                lt_antecedentes = Antecedente.objects.filter(
                    grupoAntecedente_id=grupo_antecedente.id)
                data["lt_antecedentes"] = [{"id": x.id, "descripcion": x.descripcion}
                                           for x in lt_antecedentes]
                data["result"] = "ok"
                return JsonResponse(data, safe=False)
        else:
            id_paciente = request.GET.get("id_paciente", "")
            historia = None
            try:
                historia = Historia.objects.get(pk=int(id_paciente))
            except Exception as ex:
                pass
            if historia:
                data['historia'] = historia
                data['list_historia_detalle'] = HistoriaDetalle.objects.filter(
                    historia_id=historia.id)
                data['signo_vitales'] = TomarSignoVital.objects.filter(
                    receta__paciente_id=int(id_paciente))
                print(data['signo_vitales'])
            else:
                historia = Historia.objects.create(
                    paciente_id=int(id_paciente),
                    historiaNo='0'+id_paciente,
                    notasinterna=""
                )
                data['historia'] = historia
            data['title'] = 'Historia Clinica'
            data['lt_grupo_antecedentes'] = GrupoAntecedente.objects.filter(
                estado=True)
            return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                historia = Historia.objects.get(
                    pk=int(request.POST['id_paciente']))
                historia.notasinterna = request.POST['notas_internas']
                historia.save()
                HistoriaDetalle.objects.filter(
                    historia_id=historia.id).delete()
                lt_historia = json.loads(request.POST['lt_historia'])
                for detalle_historia in lt_historia:
                    print(detalle_historia["id_antecedente"])
                    HistoriaDetalle.objects.create(
                        historia_id=historia.id,
                        GrupoAntecedente_id=int(
                            detalle_historia["id_grupo_antecedente"]),
                        antecedente_id=int(
                            detalle_historia["id_antecedente"]),
                        descripcion=detalle_historia["descripcion"],
                    )
                data["result"] = "ok"
                # form = self.form_class(request.POST)
                # form.save()

        except Exception as ex:
            data["error"] = str(ex)
        return JsonResponse(data, safe=False)
        # return HttpResponse(json.dumps(data), content_type="application/json")


class HistoriaView(View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = "atencion/historia/historia.html"

    def get(self, request, *args, **kwargs):
        data = {}
        action = request.GET.get("action")
        if action:
            if action == "data_antecedente":
                id_grupo_antecedente = request.GET.get("id_grupo_antecedente")
                grupo_antecedente = GrupoAntecedente.objects.get(
                    pk=int(id_grupo_antecedente))
                lt_antecedentes = Antecedente.objects.filter(
                    grupoAntecedente_id=grupo_antecedente.id)
                data["lt_antecedentes"] = [{"id": x.id, "descripcion": x.descripcion}
                                           for x in lt_antecedentes]
                data["result"] = "ok"
                return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            id_paciente = request.GET.get("id_paciente", "")
            historia = None
            try:
                historia = Historia.objects.get(pk=int(id_paciente))
            except Exception as ex:
                pass
            if historia:
                data['historia'] = historia

                data['lt_historia_detalle'] = HistoriaDetalle.objects.filter(
                    historia_id=historia.id)
            else:
                historia = Historia.objects.create(
                    paciente_id=int(id_paciente),
                    historiaNo='0'+id_paciente,
                    notasinterna=""
                )
                data['historia'] = historia
            data['title'] = 'Historia Clinica'
            data['lt_grupo_antecedentes'] = GrupoAntecedente.objects.filter(
                estado=True)
            return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                historia = Historia.objects.get(
                    pk=int(request.POST['id_paciente']))
                historia.notasinterna = request.POST['notas_internas']
                historia.save()
                HistoriaDetalle.objects.filter(
                    historia_id=historia.id).delete()
                lt_historia = json.loads(request.POST['lt_historia'])
                for detalle_historia in lt_historia:
                    print(detalle_historia["id_antecedente"])
                    HistoriaDetalle.objects.create(
                        historia_id=historia.id,
                        GrupoAntecedente_id=int(
                            detalle_historia["id_grupo_antecedente"]),
                        antecedente_id=int(
                            detalle_historia["id_antecedente"]),
                        descripcion=detalle_historia["descripcion"],
                    )
                data["result"] = "ok"
                # form = self.form_class(request.POST)
                # form.save()

        except Exception as ex:
            data["error"] = str(ex)
        return JsonResponse(data, safe=False)
        # return HttpResponse(json.dumps(data), content_type="application/json")
