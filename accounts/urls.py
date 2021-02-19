# from django.contrib import admin
from django.urls import path, include
from accounts.views import (
	UserLogin,
	UserCreate,
	UserChange,
	UserDelete,
	UserListView,
	# PasswordChange,
	# PasswordReset,
	# PasswordResetConfirm,
	# PasswordResetComplete,
)

# from django.contrib.auth.views import (
# 	PasswordResetDoneView,
# )


urlpatterns = [
	path('login/', UserLogin.as_view(), name='login'),
	path('usuarios/', UserListView.as_view(), name='users'),
	path('user-new/', UserCreate.as_view(), name='user-new'),
	path('<int:pk>/update/', UserChange.as_view(), name='user-change'),
	path('<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
	path('', include('django.contrib.auth.urls')),
	# path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
	# path('password-change/', PasswordChange.as_view(), name='password-change'),
	# path('password-reset/', PasswordReset.as_view(), name='password-reset'),
	# path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name="password_reset_confirm"),
	# path('reset/done/', PasswordResetComplete.as_view(), name='password-reset-complete'),
]
