from django import forms

from professores.models import Professor


class ProfessorForm(forms.ModelForm):

	class Meta:
		model = Professor

		exclude = [
			'professor_id',
			'created',
			'modified'
		]
