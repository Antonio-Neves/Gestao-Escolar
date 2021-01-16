from django.urls import path
from alunos.views import (
	AlunoIndexView,
	AlunoNewView,
	AlunoUpdateView,
	AlunoDeleteView,
)


urlpatterns = [
	path('', AlunoIndexView.as_view(), name='index-aluno'),
	path('aluno-novo/', AlunoNewView.as_view(), name='aluno-novo'),
	path('<int:pk>/alterar/', AlunoUpdateView.as_view(), name='aluno-alterar'),
	path('<int:pk>/delete', AlunoDeleteView.as_view(), name='aluno-delete'),
]