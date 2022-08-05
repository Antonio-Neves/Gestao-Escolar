from django.urls import path

from turmas.views import TurmaNewView


urlpatterns = [
	path('turma-nova', TurmaNewView.as_view(), name='turma-nova')
]
