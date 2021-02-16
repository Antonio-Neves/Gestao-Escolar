from django.urls import path
from professores.views import (
	IndexProfessorView,
	ProfessorListView,
	ProfessorNewView,
	ProfessorUpdateView,
	ProfessorDeleteView,
)


urlpatterns = [
	path('', IndexProfessorView.as_view(), name='index-professor'),
	path('professores/', ProfessorListView.as_view(), name='professores'),
	path('professor-novo/', ProfessorNewView.as_view(), name='professor-novo'),
	path('<int:pk>/alterar/', ProfessorUpdateView.as_view(), name='professor-alterar'),
	path('<int:pk>/delete/', ProfessorDeleteView.as_view(), name='professor-delete'),
]
