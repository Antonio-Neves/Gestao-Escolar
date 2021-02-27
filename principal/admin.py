from django.contrib import admin

from principal.models import AnoLetivo, EtapaBasica, AnoEscolar
from principal.forms import AnoLetivoForm, EtapaBasicaForm


admin.site.register(AnoLetivo)
admin.site.register(EtapaBasica)
admin.site.register(AnoEscolar)
