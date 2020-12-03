from django.urls import path
from administracao.views import (
	IndexAdministracaoView
)


urlpatterns = [
	path('', IndexAdministracaoView.as_view(), name='index-administracao')
]
