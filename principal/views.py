from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from principal.models import AnoLetivo, AnoEscolar, EtapaBasica, Disciplina
from principal.forms import AnoLetivoForm, AnoEscolarForm, EtapaBasicaForm, DisciplinaForm

# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersAdSe


# --- Admin views --- #
class AnoLetivoNewView(BaseAdminUsersAdSe, CreateView):
	model = AnoLetivo
	template_name = 'principal/ano-letivo-novo.html'
	form_class = AnoLetivoForm
	success_url = reverse_lazy('etapa-basica-nova')
	success_message = 'Novo ano letivo criado com sucesso'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['anos_letivos'] = AnoLetivo.objects.all()

		return context


class EtapaBasicaNewView(BaseAdminUsersAdSe, CreateView):
	model = EtapaBasica
	template_name = 'principal/etapa-basica-nova.html'
	form_class = EtapaBasicaForm
	success_url = reverse_lazy('etapa-basica-nova')
	success_message = 'Nova etapa basica criada com sucesso'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['etapas_basicas'] = EtapaBasica.objects.all()
		context['anos_letivos'] = AnoLetivo.objects.all()

		return context


class AnoEscolarNewView(BaseAdminUsersAdSe, CreateView):
	model = AnoEscolar
	template_name = 'principal/ano-escolar-novo.html'
	form_class = AnoEscolarForm
	success_url = reverse_lazy('ano-escolar-novo')
	success_message = 'Novo ano escolar criado com sucesso'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['anos_letivos'] = AnoLetivo.objects.all()
		context['anos_escolares'] = AnoEscolar.objects.all()
		# context['etapas_basicas'] = EtapaBasica.objects.all()

		return context


# --- Lists views --- #
class AnoLetivoListView(BaseAdminUsersAdSe, ListView):
	model = AnoLetivo
	template_name = 'principal/anos-letivos.html'


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
	pass


class DisciplinaDeleteView(BaseAdminUsersAdSe, ListView):
	model = Disciplina
	template_name = 'principal/disciplinas.html'
