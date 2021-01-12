from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import CustomUser
from django.contrib.auth.views import (
	PasswordChangeView,
	PasswordResetView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
	)


class UserCreate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
	model = CustomUser
	form_class = CustomUserCreateForm
	template_name = 'accounts/user-new.html'
	success_url = '/index-manager/'
	success_message = 'Novo usuário cadastrado com sucesso'

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""

		authorized_admin_access = ['ad', 'se']  # lista de acesso a funções administrativas

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


class UserChange(SuccessMessageMixin, UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	template_name = 'accounts/user-change.html'
	success_url = '/'
	success_message = 'O seu perfil foi alterado com sucesso'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class UserDelete(SuccessMessageMixin, DeleteView):
	model = CustomUser
	success_url = '/'
	template_name = 'accounts/user-delete.html'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
	template_name = 'accounts/password-change.html'
	success_url = '/'
	success_message = 'A sua senha foi alterada com sucesso'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
	template_name = 'accounts/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
	success_message = 'A sua senha foi alterada corretamente. Faça login para começar'
	# success_url = '/accounts/login'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
	template_name = 'registration/login.html'
	success_message = 'A sua senha foi alterada corretamente. Faça login para começar'
