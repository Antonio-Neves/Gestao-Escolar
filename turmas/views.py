from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Case, CharField, Value, When

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from turmas.models import Turma
from turmas.forms import TurmaForm

# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersAdSe


class TurmaNewView(BaseAdminUsersAdSe, CreateView):
	model = Turma
	template_name = 'turmas/turma-nova.html'
	form_class = TurmaForm
	success_url = reverse_lazy('turma-nova')
	success_message = 'Turma criada com sucesso'
