from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from unidecode import unidecode  # normalize strings Csii

from alunos.models import Aluno
from alunos.forms import AlunoForm
from accounts.models import CustomUser
# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersAdSe


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


# --- Admin views --- #
class AlunoInfoView(BaseAdminUsersAdSe):
	pass


class AlunoNewView(BaseAdminUsersAdSe, CreateView):
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


class AlunoUpdateView(BaseAdminUsersAdSe, UpdateView):
	model = Aluno
	form_class = AlunoForm
	template_name = 'alunos/aluno-alterar.html'
	success_message = 'As alterações foram efectuadas com sucesso'

	def get_success_url(self):
		"""
		Reverse to the form of created user, (update view).
		"""
		return reverse('aluno-alterar', kwargs={'pk': self.object.pk})


class AlunoDeleteView(BaseAdminUsersAdSe, DeleteView):
	model = Aluno
	template_name = 'alunos/aluno-delete.html'
	success_message = 'Os dados do aluno(a) foram corretamente apagados da base de dados'

	def get_success_url(self):
		"""
		Only necessary for display sucess message after delete
		"""
		messages.success(self.request, self.success_message)

		return reverse('alunos')


# --- Lists views --- #
class AlunosListView(BaseAdminUsersAdSe, ListView):
	model = Aluno
	template_name = 'alunos/alunos.html'


class AlunosEfetivoListView(BaseAdminUsersAdSe, ListView):
	model = Aluno
	template_name = 'alunos/alunos-efetivo.html'
