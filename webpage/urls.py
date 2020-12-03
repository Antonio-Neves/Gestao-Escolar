from django.urls import path
from webpage.views import (
	IndexView,
	IndexManagerView,
)


urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('index-manager/', IndexManagerView.as_view(), name='index-manager'),
]
