from django.db import models


class Municipio(models.Model):
	"""
	Populate table with 'base_municipio.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	municipio_codigo = models.CharField(
		'Código do Município',
		max_length=7,
		primary_key=True,
		unique=True
	)
	municipio_uf = models.CharField(
		'UF',
		max_length=2
	)
	municipio_nome = models.CharField(
		'Município',
		max_length=50
	)

	class Meta:
		verbose_name = 'Município'
		verbose_name_plural = 'Municípios'

	def __str__(self):
		return self.municipio_nome


class Pais(models.Model):
	"""
	Populate table with 'base_pais.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	pais_codigo = models.CharField(
		'Código do País',
		max_length=3,
		primary_key=True,
		unique=True
	)
	pais_nome = models.CharField(
		'País',
		max_length=50,
	)

	class Meta:
		verbose_name = 'País'
		verbose_name_plural = 'Países'

	def __str__(self):
		return self.pais_nome


class CursoFS(models.Model):
	"""
	Curso de Formação Superior
	Populate table with 'base_cfs.csv' in:
	BASE_ROOT
		notes_and_extras
			Tabelas necessárias
	"""
	cfs_id = models.CharField(
		'Código do Curso de Formação Superior',
		max_length=6,
		primary_key=True,
		unique=True
	)
	cfs_nome_grau = models.CharField(
		'Nome do curso de Formação Superior',
		max_length=100,
		unique=True
	)

	class Meta:
		verbose_name = 'Curso Formação Superior'
		verbose_name_plural = 'Cursos de Formação Superior'

	def __str__(self):
		return self.cfs_nome_grau
