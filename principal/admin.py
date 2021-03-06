from django.contrib import admin

from principal.models import AnoLetivo, EtapaBasica, AnoEscolar, Disciplina
from principal.forms import (
	AnoLetivoForm,
	AnoEscolarForm,
	EtapaBasicaForm,
	DisciplinaForm
)
from turmas.models import Turma

admin.site.register(AnoLetivo)
admin.site.register(EtapaBasica)
admin.site.register(AnoEscolar)
admin.site.register(Disciplina)
admin.site.register(Turma)
