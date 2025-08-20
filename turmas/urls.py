from django.urls import path

from turmas.views import TurmaNewView, ListaTurmasView



urlpatterns = [
    path('', ListaTurmasView.as_view(), name='lista-turmas'),
    path('turma-nova', TurmaNewView.as_view(), name='turma-nova'),
]
