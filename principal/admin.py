from django.contrib import admin

from principal.models import AnoLetivo, EtapaBasico, AnoEscolar
from principal.forms import AnoLetivoForm, EtapaBasicoForm


admin.site.register(AnoLetivo)
admin.site.register(EtapaBasico)
admin.site.register(AnoEscolar)
