from django import forms

from turmas.models import Turma


class TurmaForm(forms.ModelForm):

	class Meta:
		model = Turma

		exclude = [
			'turma_id',
		]
