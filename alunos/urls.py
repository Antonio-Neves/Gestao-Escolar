from django.urls import path
from alunos.views import (
	AlunoIndexView,
	AlunoNewView
)


urlpatterns = [
	path('', AlunoIndexView.as_view(), name='index-aluno'),
	path('aluno-novo/', AlunoNewView.as_view(), name='aluno-novo')
]