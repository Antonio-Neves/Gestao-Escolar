from django import forms

from principal.models import (Disciplina)


class DisciplinaForm(forms.ModelForm):

	class Meta:
		model = Disciplina

		fields = [
			'disciplina_nome',
			'disciplina_professor'
		]
