from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from professores.models import Professor
from professores.forms import ProfessorForm


class IndexProfessorView(TemplateView):
	template_name = 'professores/index-professor.html'


@method_decorator(login_required, name='dispatch')
class ProfessorNewView(SuccessMessageMixin, CreateView):
	model = Professor
	template_name = 'professores/professor-novo.html'
	form_class = ProfessorForm
	success_url = '/professores/professor-novo'
	success_message = 'Professor cadastrado com sucesso'

	def get(self, request, *args, **kwargs):

		context = {
			'professor_obj': Professor.objects.all(),
			'form': ProfessorForm()
		}

		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = ProfessorForm(request.POST)

		if form.is_valid():
			form_model = form.save(commit=False)
			form_model.save()
			form.save_m2m()
			messages.success(request, self.success_message)

			return redirect(self.success_url)

		else:
			context = {
				'aluno_obj': Professor.objects.all(),
				'form': ProfessorForm(request.POST)
			}

			return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class ProfessorUpdateView(SuccessMessageMixin, UpdateView):
	model = Professor
	form_class = ProfessorForm
	template_name = 'professores/professor-alterar.html'
	success_message = 'As alterações foram efectuadas com sucesso'

	def get_form(self, form_class=None):

		form = super(ProfessorUpdateView, self).get_form(form_class)

		return form

	def get_success_url(self):

		return reverse('professor-alterar', kwargs={'pk': self.object.pk,})


