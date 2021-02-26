from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from accounts.models import CustomUser
from base.base_admin_permissions import BaseAdminUsersAdSe

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.views import (
	LoginView,
	# PasswordChangeView,
	# PasswordResetView,
	# PasswordResetConfirmView,
	# PasswordResetCompleteView,
	)


class UserLogin(SuccessMessageMixin, LoginView):
	template_name = 'accounts/login.html'

	def get(self, request, *args, **kwargs):

		if self.request.user.is_authenticated:
			return redirect('index-manager')

		else:
			return self.render_to_response(self.get_context_data())


class UserCreate(BaseAdminUsersAdSe, CreateView):
	model = CustomUser
	form_class = CustomUserCreateForm
	template_name = 'accounts/user-new.html'
	success_url = reverse_lazy('index-manager')
	success_message = 'Novo usuário cadastrado com sucesso'


class UserChange(BaseAdminUsersAdSe, UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	template_name = 'accounts/user-change.html'
	success_url = reverse_lazy('users')
	success_message = 'Os dados do usuário foram alterados com sucesso'


class UserDelete(BaseAdminUsersAdSe, DeleteView):
	model = CustomUser
	template_name = 'accounts/user-delete.html'
	success_message = 'Os dados do usuário foram removidos da base de dados'

	def get_success_url(self):
		"""
		Only necessary for display sucess message after delete
		"""
		messages.success(self.request, self.success_message)

		return reverse('users')


class UserListView(BaseAdminUsersAdSe, ListView):
	model = CustomUser
	template_name = 'accounts/usuarios.html'


# class PasswordReset(SuccessMessageMixin, PasswordResetView):
# 	template_name = 'accounts/password-reset.html'
#
#
# class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
# 	success_message = 'A sua senha foi alterada corretamente. Faça login para começar'
# 	# success_url = '/accounts/login'
#
#
# class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
# 	template_name = 'accounts/password-reset-complete.html'
# 	success_message = 'A sua senha foi alterada corretamente. Faça login para começar'
#
# 	def get(self, request, *args, **kwargs):
# 		return redirect('login')
