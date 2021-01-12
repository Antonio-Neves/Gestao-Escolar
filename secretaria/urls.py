from django.urls import path
from secretaria.views import (
	IndexSecretariaView
)


urlpatterns = [
	path('', IndexSecretariaView.as_view(), name='index-secretaria')
]
