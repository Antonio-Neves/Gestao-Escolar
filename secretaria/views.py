from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView


class IndexSecretariaView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, TemplateView):
	template_name = 'secretaria/index-secretaria.html'

	def test_func(self):
		"""
		Testa se o departamento do usuario logado,
		é Administração.
		"""

		if self.request.user.department == 'se':
			return True

	def handle_no_permission(self):
		"""
		Redirecionamentos no caso do departamento do usuário logado
		não ser Administração.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')

