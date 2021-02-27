from django import forms

from principal.models import (
	AnoLetivo,
	EtapaBasica,
	AnoEscolar,
)


class AnoLetivoForm(forms.ModelForm):

	class Meta:
		model = AnoLetivo

		fields = [
			'ano_letivo_nome',
		]


class EtapaBasicaForm(forms.ModelForm):

	class Meta:
		model = EtapaBasica

		fields = [
			'etapa_basica_nome',
			'etapa_basica_ano',
		]


class AnoEscolarForm(forms.ModelForm):

	class Meta:
		model = AnoEscolar

		fields = [
			'ano_escolar_nome',
			'ano_escolar_etapa',
		]
