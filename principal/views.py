from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from principal.models import Disciplina
from principal.forms import DisciplinaForm

# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersAdSe


# --- Disciplinas --- #
class DisciplinaNewView(BaseAdminUsersAdSe, CreateView):
	model = Disciplina
	template_name = 'principal/disciplina-nova.html'
	form_class = DisciplinaForm
	success_url = reverse_lazy('disciplina-nova')
	success_message = 'Nova disciplina cadastrada com sucesso'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['disciplinas'] = Disciplina.objects.all()

		return context


class DisciplinaUpdateView(BaseAdminUsersAdSe, UpdateView):
	model = Disciplina
	form_class = DisciplinaForm
	template_name = 'principal/disciplina-update.html'
	success_url = reverse_lazy('disciplinas')
	success_message = 'Disciplina alterada com sucesso'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['disciplinas'] = Disciplina.objects.all()

		return context


class DisciplinaListView(BaseAdminUsersAdSe, ListView):
	model = Disciplina
	template_name = 'principal/disciplinas.html'
