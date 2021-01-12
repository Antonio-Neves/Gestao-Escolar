from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from unidecode import unidecode  # normalize strings Csii

from alunos.models import Aluno
from alunos.forms import AlunoForm
from accounts.models import CustomUser


class AlunoIndexView(TemplateView):
	template_name = 'alunos/index-aluno.html'


class AlunoNewView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
	model = Aluno
	template_name = 'alunos/aluno-novo.html'
	form_class = AlunoForm
	success_url = '/alunos/aluno-novo'
	success_message = 'Aluno Cadastrado com sucesso'

	def post(self, request, *args, **kwargs):

		form = self.get_form()

		if form.is_valid():

			# Create user after 'aluno' registration

			cpf1 = request.POST.get('aluno_filiacao1_cpf')
			cpf2 = request.POST.get('aluno_filiacao2_cpf')
			department = 're'

			if cpf1:  # if 'filiação1' create user

				# Data from Filiação 1 for user creation
				cpf1_split_1 = cpf1.split('.')
				cpf1_split_2 = ''.join(cpf1_split_1).split('-')
				cpf1_join = ''.join(cpf1_split_2)
				nome1_form = request.POST.get('aluno_filiacao1_nome')
				nome1_split = nome1_form.split()
				first_name1 = nome1_split[0]
				last_name1 = nome1_split[-1]
				password1 = f'{unidecode(first_name1).lower()}{cpf1_join[0:6]}'

				CustomUser.objects.create_user(
					identifier=cpf1_join,
					password=password1,
					first_name=first_name1,
					last_name=last_name1,
					department=department
				)

			if cpf2:  # if 'filiação2' create user

				# Date from Filiação 2 for user creation
				cpf2_split_1 = cpf2.split('.')
				cpf2_split_2 = ''.join(cpf2_split_1).split('-')
				cpf2_join = ''.join(cpf2_split_2)
				nome2_form = request.POST.get('aluno_filiacao2_nome')
				nome2_split = nome2_form.split()
				first_name2 = nome2_split[0]
				last_name2 = nome2_split[-1]
				password2 = f'{unidecode(first_name2).lower()}{cpf2_join[0:6]}'

				CustomUser.objects.create_user(
					identifier=cpf2_join,
					password=password2,
					first_name=first_name2,
					last_name=last_name2,
					department=department
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


class AlunoUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
	model = Aluno
	form_class = AlunoForm
	template_name = 'alunos/aluno-alterar.html'
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
		Redirect to the form of created user, (change view).
		"""

		return reverse('aluno-alterar', kwargs={'pk': self.object.pk,})
