from django.urls import path
from principal.views import AnoLetivoNewView, EtapaBasicaView, AnoEscolarView


urlpatterns = [
	path('ano-letivo-novo/', AnoLetivoNewView.as_view(), name='ano-letivo-novo'),
	path('etapa-basica-nova/', EtapaBasicaView.as_view(), name='etapa-basica-nova'),
	path('ano-escolar-novo/', AnoEscolarView.as_view(), name='ano-escolar-novo')
]
