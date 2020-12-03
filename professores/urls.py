from django.urls import path
from professores.views import (
	IndexProfessorView
)


urlpatterns = [
	path('', IndexProfessorView.as_view(), name='index-professor')
]
