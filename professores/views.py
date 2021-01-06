from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from professores.models import Professor
from professores.forms import ProfessorForm


class IndexProfessorView(TemplateView):
	template_name = 'professores/index-professor.html'


class ProfessorNewView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
	model = Professor
	template_name = 'professores/professor-novo.html'
	form_class = ProfessorForm
	success_url = '/professores/professor-novo'
	success_message = 'Professor cadastrado com sucesso'

	def test_func(self):
		"""
		Testa se o departamento do usuario logado,
		tem acesso a funções administrativas.
		"""

		authorized_admin_access = ['ad', 'se']  # lista de acesso a funções administrativas

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirecionamentos no caso do departamento do usuário logado
		não ter acesso a funções administrativas.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


class ProfessorUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
	model = Professor
	form_class = ProfessorForm
	template_name = 'professores/professor-alterar.html'
	success_message = 'As alterações foram efectuadas com sucesso'

	def test_func(self):
		"""
		Testa se o departamento do usuario logado,
		tem acesso a funções administrativas.
		"""

		authorized_admin_access = ['ad', 'se']  # lista de acesso a funções administrativas

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirecionamentos no caso do departamento do usuário logado
		não ter acesso a funções administrativas.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')

	def get_success_url(self):
		"""
		Redireciona para o mesmo formulário do aluno que está sendo alterado.
		"""

		return reverse('professor-alterar', kwargs={'pk': self.object.pk,})
