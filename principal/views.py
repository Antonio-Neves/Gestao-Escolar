from django.shortcuts import redirect, render, reverse
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
	success_url = '/principal/etapa-nova'
	success_message = 'Novo ano letivo criado com sucesso'
