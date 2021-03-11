from django.shortcuts import redirect, render, reverse
from django.db.models import Q

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from alunos.models import Aluno
from turmas.models import Turma

# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersAd
# Constants Vars
from base.constants import CURRENT_YEAR


class IndexAdministracaoView(BaseAdminUsersAd, TemplateView):
	template_name = 'administracao/index-administracao.html'


class AdministracaoSearchView(BaseAdminUsersAd, ListView):
	model = Aluno
	template_name = 'administracao/busca-ad.html'

	def get_queryset(self):
		qs = super().get_queryset()
		# users = CustomUser.objects.all()
		term = self.request.GET.get('term')

		if term:
			qs = qs.filter(
				Q(aluno_nome__istartswith=term)
				# Q(aluno_filiacao1_cpf__iexact=term) |
				# Q(aluno_filiacao2_cpf__iexact=term)
			)

			# if not qs:
			# 	qs = users.filter(first_name__istartswith=term)

			return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		turmas = Turma.objects.all().filter(
			turma_ano_escolar__ano_escolar_etapa__etapa_basica_ano__ano_letivo_nome=CURRENT_YEAR
		)

		context['turmas'] = turmas

		return context
