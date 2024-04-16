from base import constants


def templates_global_context(request):
	"""
	Return context for use in all templates.
	"""
	global_context = {
		'constant_ddd': constants.DDD,
		'constant_estado': constants.ESTADO,
		'constant_municipio': constants.MUNICIPIO,
		'constant_cep': constants.CEP,
		'constant_pais': constants.PAIS,
		'constant_current_year': constants.CURRENT_YEAR,
	}

	return global_context
