from django.shortcuts import redirect, render, reverse
from django.db.models import Case, CharField, Value, When

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from django.db.models import Q

from alunos.models import Aluno
from turmas.models import Turma
# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersSe
# Constants Vars
from base.constants import CURRENT_YEAR


class IndexSecretariaView(BaseAdminUsersSe, TemplateView):
	template_name = 'secretaria/index-secretaria.html'


class SecretariaSearchView(BaseAdminUsersSe, ListView):
	model = Aluno
	template_name = 'secretaria/busca-se.html'

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

		turmas = Turma.objects.filter(
			turma_ano_letivo=CURRENT_YEAR
		).annotate(
			ano_escolar_display=Case(
				When(turma_ano_escolar='CR', then=Value('Creche')),
				When(turma_ano_escolar='G1', then=Value('Maternal I')),
				When(turma_ano_escolar='G2', then=Value('Maternal II')),
				When(turma_ano_escolar='G3', then=Value('Maternal III')),
				When(turma_ano_escolar='G4', then=Value('Jardim I')),
				When(turma_ano_escolar='G5', then=Value('Jardim II')),
				When(turma_ano_escolar='1A', then=Value('1º Ano')),
				When(turma_ano_escolar='2A', then=Value('2º Ano')),
				When(turma_ano_escolar='3A', then=Value('3º Ano')),
				When(turma_ano_escolar='4A', then=Value('4º Ano')),
				When(turma_ano_escolar='5A', then=Value('5º Ano')),
				When(turma_ano_escolar='6A', then=Value('6º Ano')),
				When(turma_ano_escolar='7A', then=Value('7º Ano')),
				When(turma_ano_escolar='8A', then=Value('8º Ano')),
				When(turma_ano_escolar='9A', then=Value('9º Ano')),
				output_field=CharField()
			)
		).values_list(
			'ano_escolar_display',
			'turma_nome',
			'turma_etapa_basica',
			'turma_aluno'
		)

		context['turmas'] = turmas

		return context
