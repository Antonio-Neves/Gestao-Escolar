from django.urls import path
from alunos.views import (
	AlunosView,
	AlunosEfetivoView,
	AlunoIndexView,
	AlunoNewView,
	AlunoUpdateView,
	AlunoDeleteView,
)


urlpatterns = [
	path('', AlunoIndexView.as_view(), name='index-aluno'),
	path('alunos/', AlunosView.as_view(), name='alunos'),
	path('alunos-efetivo/', AlunosEfetivoView.as_view(), name='alunos-efetivo'),
	path('aluno-novo/', AlunoNewView.as_view(), name='aluno-novo'),
	path('<int:pk>/alterar/', AlunoUpdateView.as_view(), name='aluno-alterar'),
	path('<int:pk>/delete', AlunoDeleteView.as_view(), name='aluno-delete'),
]