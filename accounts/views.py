from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import CustomUser
from django.contrib.auth.views import (
	LoginView,
	PasswordChangeView,
	# PasswordResetView,
	# PasswordResetConfirmView,
	# PasswordResetCompleteView,
	)


class UserLogin(SuccessMessageMixin, LoginView):
	template_name = 'accounts/login.html'


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

		authorized_admin_access = ['ad', 'se']  # list of the authorized departments

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


class UserChange(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	template_name = 'accounts/user-change.html'
	success_message = 'Os dados do usuário foram alterados com sucesso'

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""

		authorized_admin_access = ['ad', 'se']  # list of the authorized departments

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')

	def get_success_url(self):
		"""
		Redirect to the form of created user, (change view).
		"""

		return reverse('user-change', kwargs={'pk': self.object.pk,})


class UserDelete(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
	model = CustomUser
	success_url = '/index-manager/'
	template_name = 'accounts/user-delete.html'

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""

		authorized_admin_access = ['ad', 'se']  # list of the authorized departments

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


class PasswordChange(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, PasswordChangeView):
	template_name = 'accounts/password-change.html'
	success_url = '/index-manager/'
	success_message = 'A senha do usuário foi alterada com sucesso'

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""

		authorized_admin_access = ['ad', 'se']  # list of the authorized departments

		if self.request.user.department in authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""

		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


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
