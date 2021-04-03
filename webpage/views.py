from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


def error_403(request, exception):
	data = {}
	return render(request, 'webpage/403.html', data)


def error_404(request, exception):
	data = {}
	return render(request, 'webpage/404.html', data)


def error_500(request, exception=None):
	data = {}
	return render(request, 'webpage/500.html', data)


class IndexView(TemplateView):
	template_name = 'webpage/index.html'


class IndexManagerView(TemplateView):

	def get(self, request, *args, **kargs):
		"""
		After user login, redirect for respective dashboard,
		depending on the department
		"""

		department = {
			'ad': 'administracao',
			'fi': 'financeiro',
			'se': 'secretaria',
			'pr': 'professor',
			're': 'responsavel',
			'al': 'aluno',
		}

		if request.user.is_authenticated:

			template = department[request.user.department]
			return redirect('index-{}'.format(template))

		else:
			return redirect('login')
			# return render(request, 'webpage/index.html')
