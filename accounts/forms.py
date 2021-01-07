from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserCreateForm(UserCreationForm):

	class Meta():
		model = CustomUser
		fields = ('first_name', 'last_name', 'username', 'department')
		labels = {'username': 'Usuário'}

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.identifier = self.cleaned_data["username"]

		if commit:
			user.save()

		return user


class CustomUserChangeForm(UserChangeForm):

	class Meta():
		model = CustomUser
		fields = ('first_name', 'last_name', 'identifier', 'department')

	def save(self, commit=True):
		user = super().save(commit=False)
		user.username = self.cleaned_data["identifier"]

		if commit:
			user.save()

		return user


# class CustomUserCreateForm(UserCreationForm):
#
# 	class Meta():
# 		model = CustomUser
# 		fields = ('first_name', 'last_name', 'username', 'department')
# 		labels = {'username': 'Username/Email'}
#
# 	def save(self, commit=True):
# 		user = super().save(commit=False)
# 		user.set_password(self.cleaned_data["password1"])
# 		user.email = self.cleaned_data["username"]
#
# 		if commit:
# 			user.save()
#
# 		return user
#
#
# class CustomUserChangeForm(UserChangeForm):
#
# 	class Meta():
# 		model = CustomUser
# 		fields = ('first_name', 'last_name', 'email', 'department')
#
# 	def save(self, commit=True):
# 		user = super().save(commit=False)
# 		user.username = self.cleaned_data["email"]
#
# 		if commit:
# 			user.save()
#
# 		return user
