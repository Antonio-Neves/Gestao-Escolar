from django.urls import path
from financeiro.views import (
	IndexFinanceiroView
)


urlpatterns = [
	path('', IndexFinanceiroView.as_view(), name='index-financeiro')
]
