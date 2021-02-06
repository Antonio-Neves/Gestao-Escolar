from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.views.generic.base import TemplateView
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from unidecode import unidecode  # normalize strings Csii

from alunos.models import Aluno
from alunos.forms import AlunoForm
from accounts.models import CustomUser


def create_user_after_registration(
		username, password, first_name, last_name, department):
	"""
	Create user after aluno registration
	"""
	CustomUser.objects.create_user(
		username=username,
		password=password,
		first_name=first_name,
		last_name=last_name,
		department=department
	)


def data_processing_user_creation(cpf, name_form, department):
	"""
	Processing data for user creation
	"""

	cpf_split_1 = cpf.split('.')
	cpf_split_2 = ''.join(cpf_split_1).split('-')
	cpf_join = ''.join(cpf_split_2)
	name_split = name_form.split()
	first_name = name_split[0]
	last_name = name_split[-1]
	password = f'{unidecode(first_name).lower()}{cpf_join[0:6]}'

	create_user_after_registration(
		cpf_join, password, first_name, last_name, department)


# --- General views --- #
class AlunoIndexView(TemplateView):
	template_name = 'alunos/index-aluno.html'


class BaseAdminUsers(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, View):
	"""
	Base class for test if user department have authorized access to
	admin functions.
	And display sucess messages
	- Administração
	- Secretaria
	"""

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""
		authorized_admin_access = ['ad', 'se']  # list for admin access

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""
		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


# --- Admin views --- #
class AlunoInfoView(BaseAdminUsers):
	pass


class AlunoNewView(BaseAdminUsers, CreateView):
	model = Aluno
	template_name = 'alunos/aluno-novo.html'
	form_class = AlunoForm
	success_url = '/alunos/aluno-novo'
	success_message = 'Aluno Cadastrado com sucesso'

	def post(self, request, *args, **kwargs):

		form = self.get_form()

		if form.is_valid():

			# Data for user creation after 'aluno' registration
			cpf1 = request.POST.get('aluno_filiacao1_cpf')
			cpf2 = request.POST.get('aluno_filiacao2_cpf')
			# Test if 'Filiação CPF' of new 'Aluno' exists in 'Aluno' table
			cpf1_qs = Aluno.objects.filter(aluno_filiacao1_cpf=cpf1)
			cpf2_qs = Aluno.objects.filter(aluno_filiacao2_cpf=cpf2)

			# if 'filiação1' in form and not already exist in 'User model' create user
			if cpf1 and not cpf1_qs:

				# Data from Filiação 1 for user creation
				name1_form = request.POST.get('aluno_filiacao1_nome')

				data_processing_user_creation(cpf1, name1_form, 're')

			# if 'filiação2' in form and not already exist in 'User model' create user
			if cpf2 and not cpf2_qs:

				# Data from Filiação 2 for user creation
				name2_form = request.POST.get('aluno_filiacao2_nome')

				data_processing_user_creation(cpf2, name2_form, 're')

			return self.form_valid(form)

		else:
			return self.form_invalid(form)


class AlunoUpdateView(BaseAdminUsers, UpdateView):
	model = Aluno
	form_class = AlunoForm
	template_name = 'alunos/aluno-alterar.html'
	success_message = 'As alterações foram efectuadas com sucesso'

	def get_success_url(self):
		"""
		Reverse to the form of created user, (update view).
		"""
		return reverse('aluno-alterar', kwargs={'pk': self.object.pk})


class AlunoDeleteView(BaseAdminUsers, DeleteView):
	model = Aluno
	template_name = 'alunos/aluno-delete.html'
	# success_url = '/alunos/alunos'
	success_message = 'O aluno foi corretamente apagado da base de dados'

	def get_success_url(self):
		"""
		Only necessary for display sucess message after delete
		"""
		messages.success(self.request, self.success_message)

		return reverse('alunos')


# --- Lists views --- #
class AlunosListView(BaseAdminUsers, ListView):
	model = Aluno
	template_name = 'alunos/alunos.html'


class AlunosEfetivoListView(BaseAdminUsers, ListView):
	model = Aluno
	template_name = 'alunos/alunos-efetivo.html'
