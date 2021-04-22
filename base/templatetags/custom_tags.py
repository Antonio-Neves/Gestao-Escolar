from django import template
from base.constants import CEP, MUNICIPIO

register = template.Library()


@register.simple_tag
def set_constant_municipio(municipio):
	municipio = MUNICIPIO

	return municipio


@register.simple_tag
def set_constant_cep(cep):
	cep = CEP

	return cep
