from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreateForm
	form = CustomUserChangeForm
	model = CustomUser

	list_display = (
		'username',
		'first_name',
		'last_name',
		'department',
		'is_staff',
	)

	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Personal information',
		 {'fields': ('first_name', 'last_name', 'department')}),
		('Permissions', {
			'fields': (
				'is_active',
				'is_staff',
				'is_superuser',
				'groups',
				'user_permissions'
			)
		}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)


# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
# 	add_form = CustomUserCreateForm
# 	form = CustomUserChangeForm
# 	model = CustomUser
#
# 	list_display = (
# 		'first_name',
# 		'last_name',
# 		'department',
# 		'email',
# 		'is_staff',
# 	)
#
# 	fieldsets = (
# 		(None, {'fields': ('email', 'password')}),
# 		('Personal information',
# 		 {'fields': ('first_name', 'last_name', 'department')}),
# 		('Permissions', {
# 			'fields': ('is_active',
# 					   'is_staff',
# 					   'is_superuser',
# 					   'groups',
# 					   'user_permissions')
# 		}),
# 		('Important dates', {'fields': ('last_login', 'date_joined')}),
# 	)
