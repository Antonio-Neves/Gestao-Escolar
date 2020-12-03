from django.views.generic.base import TemplateView


class IndexResponsavelView(TemplateView):
	template_name = 'responsaveis/index-responsavel.html'
