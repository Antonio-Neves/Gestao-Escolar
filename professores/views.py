from django.views.generic.base import TemplateView


class IndexProfessorView(TemplateView):
	template_name = 'professores/index-professor.html'
