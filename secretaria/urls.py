from django.urls import path
from secretaria.views import index_secretaria_view


urlpatterns = [
	path('', index_secretaria_view, name='index-secretaria')
]
