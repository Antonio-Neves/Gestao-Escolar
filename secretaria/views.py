from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView
from django.views.generic import View, ListView

from django.db.models import Q

from alunos.models import Aluno
from accounts.models import CustomUser


class BaseSecretaria(
	LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, View):
	"""
	Base class for test if user department have authorized access to
	admin functions.
	And display sucess messages
	- Secretaria
	"""

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""
		if self.request.user.department == 'se':
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""
		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


class IndexSecretariaView(BaseSecretaria, TemplateView):
	template_name = 'secretaria/index-secretaria.html'


class SecretariaSearchView(BaseSecretaria, ListView):
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
