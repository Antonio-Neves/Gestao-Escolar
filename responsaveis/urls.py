from django.urls import path
from responsaveis.views import (
	IndexResponsavelView
)


urlpatterns = [
	path('', IndexResponsavelView.as_view(), name='index-responsavel')
]
