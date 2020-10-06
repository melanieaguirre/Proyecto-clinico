from django.urls import path
from .views import *
from .receta import *

app_name = "atencion"
urlpatterns = [
    path('historia/', HistoriaView2.as_view(), name='historia'),
    path('receta/', RecetaView.as_view(), name='receta'),
]
