from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
	template_name = 'webpage/index.html'


class IndexManagerView(TemplateView):

	def get(self, request, *args, **kargs):
		"""
		After user login, redirect for respective dashboard,
		depending on the department
		"""

		department = {
			'AD': 'administracao',
			'FI': 'financeiro',
			'SE': 'secretaria',
			'PR': 'professor',
			'RE': 'responsavel',
			'AL': 'aluno',
		}

		if request.user.is_authenticated:

			template = department[request.user.department]
			return redirect('index-{}'.format(template))

		else:
			return render(request, 'webpage/index.html')

