from django.urls import path
from professores.views import (
	IndexProfessorView,
	ProfessorNewView,
	ProfessorUpdateView
)


urlpatterns = [
	path('', IndexProfessorView.as_view(), name='index-professor'),
	path('professor-novo/', ProfessorNewView.as_view(), name='professor-novo'),
	path('<int:pk>/alterar/', ProfessorUpdateView.as_view(), name='professor-alterar')
]
