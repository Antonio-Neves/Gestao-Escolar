from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexFinanceiroView(TemplateView):
	template_name = 'financeiro/index-financeiro.html'



