from django import forms

from principal.models import (
	AnoLetivo,
	EtapaBasico,
	AnoEscolar,
)


class AnoLetivoForm(forms.ModelForm):

	class Meta:
		model = AnoLetivo

		fields = [
			'ano_letivo_nome',
		]


class EtapaBasicoForm(forms.ModelForm):

	class Meta:
		model = EtapaBasico

		fields = [
			'etapa_basico_nome',
			'etapa_basico_ano',
		]


class AnoEscolarForm(forms.ModelForm):

	class Meta:
		model = AnoEscolar

		fields = [
			'ano_escolar_nome',
			'ano_escolar_etapa',
		]
