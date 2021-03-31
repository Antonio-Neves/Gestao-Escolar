from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from unidecode import unidecode  # normalize strings Csii

from professores.models import Professor
from professores.forms import ProfessorForm
from accounts.models import CustomUser
# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersAdSe, BaseAdminUsersPr


# --- General views --- #
class IndexProfessorView(BaseAdminUsersPr, TemplateView):
	template_name = 'professores/index-professor.html'


# --- Admin views --- #
class ProfessorNewView(BaseAdminUsersAdSe, CreateView):
	model = Professor
	template_name = 'professores/professor-novo.html'
	form_class = ProfessorForm
	success_url = reverse_lazy('professor-novo')
	success_message = 'Professor cadastrado com sucesso'

	def post(self, request, *args, **kwargs):

		form = self.get_form()

		if form.is_valid():

			# Create user after 'professor' registration

			cpf = request.POST.get('professor_cpf')

			if cpf:  # if 'professor_cpf' create user

				# Create username from CPF
				cpf_split_1 = cpf.split('.')
				cpf_split_2 = ''.join(cpf_split_1).split('-')
				cpf_join = ''.join(cpf_split_2)
				username_professor = f'pr{cpf_join}'

				# Test if user already exists
				cpf_qs = CustomUser.objects.filter(username=username_professor)

				if not cpf_qs:

					# Create password from 'professor' name
					nome_form = request.POST.get('professor_nome')
					nome_split = nome_form.split()
					first_name = nome_split[0]
					if len(nome_split) > 1:
						last_name = nome_split[-1]
					else:
						last_name = 'sem sobrenome'
					password = f'{unidecode(first_name).lower()}{cpf_join[0:6]}'

					CustomUser.objects.create_user(
						username=username_professor,
						password=password,
						first_name=first_name,
						last_name=last_name,
						department='pr'
					)

			return self.form_valid(form)

		else:
			context = {'form': form}
			return render(request, self.template_name, context)


# TODO update user after 'professor' update
class ProfessorUpdateView(BaseAdminUsersAdSe, UpdateView):
	model = Professor
	form_class = ProfessorForm
	template_name = 'professores/professor-alterar.html'
	success_message = 'As alterações foram efectuadas com sucesso'

	def get_success_url(self):
		"""
		Redirect to the form of created 'professor', (change view).
		"""

		return reverse('professor-alterar', kwargs={'pk': self.object.pk,})


# TODO delete user after 'professor' delete
class ProfessorDeleteView(BaseAdminUsersAdSe, DeleteView):
	model = Professor
	template_name = 'professores/professor-delete.html'
	success_message = 'O dados do Professor(a) foram corretamente apagados da base de dados'

	def get_success_url(self):
		"""
		Only necessary for display sucess message after delete
		"""
		messages.success(self.request, self.success_message)

		return reverse('professores')


# --- Lists views --- #
class ProfessorListView(BaseAdminUsersAdSe, ListView):
	model = Professor
	template_name = 'professores/professores.html'
