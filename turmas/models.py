from django.db import models

from principal.models import AnoEscolar


class Turma(models.Model):

	turma_id = models.AutoField(
		primary_key=True
	)
	turma_ano_escolar = models.ForeignKey(
		AnoEscolar,
		verbose_name='Ano Escolar',
		on_delete=models.DO_NOTHING,
		related_name='anoescolar'

	)


