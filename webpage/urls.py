from django.urls import path
from django.views.generic.base import TemplateView
from webpage.views import (
	IndexView,
	IndexManagerView,
)


urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('index-manager/', IndexManagerView.as_view(), name='index-manager'),
	# path(
	# 	'robots.txt',
	# 	TemplateView.as_view(
	# 		template_name="webpage/robots.txt",
	# 		content_type="text/plain"
	# 	),
    # ),
	# path(
	# 	'sitemap.xml',
	# 	TemplateView.as_view(
	# 		template_name="webpage/sitemap.xml",
	# 		content_type="text/xml"
	# 	),
    # )
]
