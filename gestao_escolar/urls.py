"""gestao_escolar URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', include('webpage.urls')),
	path('usuarios/', include('accounts.urls')),
	path('administracao/', include('administracao.urls')),
	path('alunos/', include('alunos.urls')),
	path('financeiro/', include('financeiro.urls')),
	path('principal/', include('principal.urls')),
	path('professores/', include('professores.urls')),
	path('responsaveis/', include('responsaveis.urls')),
	path('secretaria/', include('secretaria.urls')),
	path('turmas/', include('turmas.urls')),
	path('admin_site/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Django Debug toolbar, only in development
if settings.DEBUG:
	import debug_toolbar
	urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

handler403 = 'webpage.views.error_403'
handler404 = 'webpage.views.error_404'
handler500 = 'webpage.views.error_500'
