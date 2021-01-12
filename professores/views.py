from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from unidecode import unidecode  # normalize strings Csii

from professores.models import Professor
from professores.forms import ProfessorForm
from accounts.models import CustomUser


class IndexProfessorView(TemplateView):
	template_name = 'professores/index-professor.html'


class ProfessorNewView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
	model = Professor
	template_name = 'professores/professor-novo.html'
	form_class = ProfessorForm
	success_url = '/professores/professor-novo'
	success_message = 'Professor cadastrado com sucesso'

	def post(self, request, *args, **kwargs):

		form = self.get_form()

		if form.is_valid():

			# Create user after 'professor' registration

			cpf = request.POST.get('professor_cpf')

			if cpf:  # if 'professor_cpf' create user

				# Data from 'Professor' for user creation
				cpf_split_1 = cpf.split('.')
				cpf_split_2 = ''.join(cpf_split_1).split('-')
				cpf_join = ''.join(cpf_split_2)
				nome_form = request.POST.get('professor_nome')
				nome_split = nome_form.split()
				first_name = nome_split[0]
				last_name = nome_split[-1]
				password1 = f'{unidecode(first_name).lower()}{cpf_join[0:6]}'

				CustomUser.objects.create_user(
					identifier=cpf_join,
					password=password1,
					first_name=first_name,
					last_name=last_name,
					department='pr'
				)

			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""

		authorized_admin_access = ['ad', 'se']  # list of the authorized departments

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
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
		Test if authenticated user can access to this view.
		"""

		authorized_admin_access = ['ad', 'se']  # list of the authorized departments

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')

	def get_success_url(self):
		"""
		Redirect to the form of created 'professor', (change view).
		"""

		return reverse('professor-alterar', kwargs={'pk': self.object.pk,})
