from django.urls import path
from principal.views import (
	DisciplinaNewView,
	DisciplinaUpdateView,
	DisciplinaListView,
)

urlpatterns = [
	path('disciplina-nova/', DisciplinaNewView.as_view(), name='disciplina-nova'),
	path('<int:pk>/alterar', DisciplinaUpdateView.as_view(), name='disciplina-update'),
	path('disciplinas/', DisciplinaListView.as_view(), name='disciplinas'),
]
