from django.urls import path
from administracao.views import (
	IndexAdministracaoView,
	AdministracaoSearchView,
)


urlpatterns = [
	path('', IndexAdministracaoView.as_view(), name='index-administracao'),
	path('busca/', AdministracaoSearchView.as_view(), name='busca-ad'),
]
