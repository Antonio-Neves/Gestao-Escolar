"""
Models for User Account

- The username is the Email and not a name.
- The user is staff
- The user must belong to a department
"""

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, username, password, **extra_fields):

		if not username:
			raise ValueError('É necessário preencher o campo usuário')

		# identifier = self.normalize_email(identifier)
		user = self.model(username=username, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, password=None, **extra_fields):

		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, password, **extra_fields)

	def create_superuser(self, username, password, **extra_fields):

		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser need to be is_superuser=True')

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser need to be is_staff=True')

		return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):

	DEPARTMENT_CHOICES = (
		('ad', 'Administração'),
		('fi', 'Financeiro'),
		('se', 'Secretaria'),
		('pr', 'Professor'),
		('re', 'Responsável'),
		('al', 'Aluno')
	)

	is_staff = models.BooleanField('Team member', default=True)
	department = models.CharField(
		'Departamento',
		max_length=2,
		choices=DEPARTMENT_CHOICES
	)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'department']

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
		ordering = ['first_name']

	def __str__(self):
		return self.username

	objects = UserManager()
