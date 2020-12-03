from django.views.generic.base import TemplateView


class IndexAdministracaoView(TemplateView):
	template_name = 'administracao/index-administracao.html'
