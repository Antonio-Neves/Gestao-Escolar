from django.urls import path
from secretaria.views import (
	IndexSecretariaView,
	SecretariaSearchView,
)


urlpatterns = [
	path('', IndexSecretariaView.as_view(), name='index-secretaria'),
	path('busca/', SecretariaSearchView.as_view(), name='busca-se'),
]
