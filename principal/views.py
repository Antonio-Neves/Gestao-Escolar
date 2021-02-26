from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from principal.models import AnoLetivo, AnoEscolar, EtapaBasico
from principal.forms import AnoLetivoForm, AnoEscolarForm, EtapaBasicoForm

# Classes to control admin acess and success messages
from base.base_admin_permissions import BaseAdminUsersAdSe


class AnoLetivoNewView(BaseAdminUsersAdSe, CreateView):
	model = AnoLetivo
	template_name = 'principal/ano-letivo-novo.html'
	form_class = AnoLetivoForm
	success_url = reverse_lazy('etapa-basica-nova')
	success_message = 'Novo ano letivo criado com sucesso'


class EtapaBasicaView(BaseAdminUsersAdSe, CreateView):
	model = EtapaBasico
	template_name = 'principal/etapa-basica-nova.html'
	form_class = EtapaBasicoForm
	success_url = reverse_lazy('etapa-basica-nova')
	success_message = 'Nova etapa basica criada com sucesso'




class AnoEscolarView(BaseAdminUsersAdSe, CreateView):
	model = AnoEscolar
	template_name = 'principal/ano-escolar-novo.html'
	form_class = AnoEscolarForm
	success_url = reverse_lazy('ano-escolar-novo')
	success_message = 'Novo ano escolar criado com sucesso'
