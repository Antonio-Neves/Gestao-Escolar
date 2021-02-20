"""
	Base classes for test if user is authenticathed and
	the department have authorized access to admin functions.
	And display sucess messages.
"""

from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View


class BaseAdminUsers(
	LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, View):
	"""
	Base class for test if user department have authorized access to
	admin functions.
	And display sucess messages
	"""
	authorized_admin_access = []  # list for admin access

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""

		if self.request.user.department in self.authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""
		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('index-manager')

		return redirect('login')


class BaseAdminUsersAdSe(BaseAdminUsers):
	"""
	Departments authorized to access admin functions.
	- Administração
	- Secretaria
	"""
	authorized_admin_access = ['ad', 'se']  # list for admin access


class BaseAdminUsersAd(BaseAdminUsers):
	"""
	Departments authorized to access admin functions.
	- Administração
	- Secretaria
	"""
	authorized_admin_access = ['ad']  # list for admin access


class BaseAdminUsersSe(BaseAdminUsers):
	"""
	Departments authorized to access admin functions.
	- Secretaria
	"""
	authorized_admin_access = ['se']  # list for admin access


class BaseAdminUsersPr(BaseAdminUsers):
	"""
	Departments authorized to access admin functions.
	- Professor
	"""
	authorized_admin_access = ['pr']  # list for admin access


if __name__ == '__main__':
	pass
