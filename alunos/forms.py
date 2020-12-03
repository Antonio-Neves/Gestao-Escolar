from django import forms

from alunos.models import Aluno


class AlunoForm(forms.ModelForm):

	class Meta:
		model = Aluno

		exclude = [
			'aluno_id',
			'created',
			'modified'
		]
