from django.urls import path
from principal.views import AnoLetivoNewView


urlpatterns = [
	path('ano-letivo-novo/', AnoLetivoNewView.as_view(), name='ano-letivo-novo')
]
