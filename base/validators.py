"""
Module with Validators for validators attributes fields in models
"""

from django.core.exceptions import ValidationError
from datetime import date


# --- General Validators --- #
def validate_digits(value):
	if not value.isdigit():
		raise ValidationError('Só aceita números.')

	else:
		return value


def validate_no_digits(value):
	if any(n.isdigit() for n in value):
		raise ValidationError('Este campo não aceita números')

	else:
		return value


def validate_data(value):

	if len(value) != 10:
		raise ValidationError('A data está errada')

	else:
		return value


def validate_year(value):

	if len(value) != 4:
		raise ValidationError('São necessários 4 digitos')

	else:
		return value


# --- Documents Validators --- #
def validate_cpf(value):

	if len(value) != 14:
		raise ValidationError('O CPF necessita 11 números')

	else:
		return value


def validate_nis(value):

	if len(value) != 11:
		raise ValidationError('O NIS necessita 11 números')

	else:
		return value


def validate_certidao_nascimento(value):

	if len(value) != 40:
		raise ValidationError('A certidão necessita 32 números')

	else:
		return value


# --- Contact Validators --- #
def validate_cep(value):

	if len(value) != 9:
		raise ValidationError('O CEP necessita de 8 números')

	else:
		return value


def validate_ddd(value):
	if len(value) != 2:
		raise ValidationError('O DDD necessita ter 2 números')

	else:
		return value


def validate_phone(value):

	if len(value) != 9:
		raise ValidationError('O telefone necessita ter 9 números')

	else:
		return value


# --- Aluno Validators --- #
def validate_aluno_inep(value):

	if len(value) != 12:
		raise ValidationError('O Inep necessita 12 números')

	else:
		return value


# --- Professor Validators --- #
def validate_professor_inep(value):

	if len(value) != 12:
		raise ValidationError('O Inep necessita 12 números')

	else:
		return value


# --- School Validators --- #
def validate_ano_letivo(value):

	if len(value) != 4:
		raise ValidationError('O Ano Letivo necessita 4 números')

	else:
		return value
