from django.db import models
# from base.validators import validate_digits, validate_ano_letivo

from professores.models import Professor


class Disciplina(models.Model):

	DISCIPLINA_CHOICES = (
		('port', 'Português'),
		('ingl', 'Inglês'),
		('espa', 'Espanhol'),
		('mate', 'Matemática'),
		('cien', 'Ciências'),
		('hist', 'História'),
		('arte', 'Artes'),
		('geog', 'Geografia'),
		('filo', 'Filosofia'),
		('edfi', 'Educação Física'),
		('enre', 'Ensino Religioso')
	)

	disciplina_id = models.AutoField(primary_key=True),
	disciplina_nome = models.CharField(
		'Disciplina',
		max_length=20,
		choices=DISCIPLINA_CHOICES
	)
	disciplina_professor = models.ForeignKey(
		Professor,
		on_delete=models.SET_NULL,
		verbose_name='Professor(a)',
		related_name='disciplinaprofessor',
		null=True
	)

	class Meta:
		verbose_name = 'Disciplina'
		verbose_name_plural = 'Disciplinas'
		constraints = [
			models.UniqueConstraint(
				fields=['disciplina_nome', 'disciplina_professor'],
				name='unica_disciplina_professor'
			)
		]
		ordering = ['disciplina_nome', 'disciplina_professor']

	def __str__(self):
		return '{} - {}'.format(
			self.get_disciplina_nome_display(),
			self.disciplina_professor
		)


# class AnoLetivo(models.Model):
# 	ano_letivo_id = models.AutoField(primary_key=True)
# 	ano_letivo_nome = models.CharField(
# 		'Ano Letivo',
# 		max_length=4,
# 		unique=True,
# 		validators=[validate_digits, validate_ano_letivo]
# 	)
#
# 	class Meta:
# 		verbose_name = 'Ano Letivo'
# 		verbose_name_plural = 'Anos Letivos'
# 		ordering = ['-ano_letivo_nome']
#
# 	def __str__(self):
# 		return self.ano_letivo_nome
#
#
# class EtapaBasica(models.Model):
#
# 	ETAPA_BASICA_CHOICES = (
# 		('IN', 'Infantil'),
# 		('F1', 'Fundamental I'),
# 		('F2', 'Fundamental II'),
# 		('EM', 'Ensino Médio')
# 	)
#
# 	etapa_basica_id = models.AutoField(primary_key=True)
# 	etapa_basica_nome = models.CharField(
# 		'Etapa de Educação',
# 		max_length=2,
# 		choices=ETAPA_BASICA_CHOICES,
# 	)
# 	etapa_basica_ano = models.ForeignKey(
# 		AnoLetivo,
# 		on_delete=models.CASCADE,
# 		verbose_name='Ano Letivo',
# 		related_name='etapabasicanome',
# 		default=''
# 	)
#
# 	class Meta:
# 		verbose_name = 'Etapa Educação Básica'
# 		verbose_name_plural = 'Etapas Educação Básica'
# 		constraints = [
# 			models.UniqueConstraint(
# 				fields=['etapa_basica_nome', 'etapa_basica_ano'],
# 				name='unica_etapa_no_ano'
# 			)
# 		]
# 		ordering = ['etapa_basica_ano', 'etapa_basica_nome']
#
# 	def __str__(self):
# 		return '{} - {}'.format(
# 			self.get_etapa_basica_nome_display(),
# 			self.etapa_basica_ano
# 		)
#
#
# class AnoEscolar(models.Model):
#
# 	ANO_ESCOLAR_CHOICES = (
# 		('CR', 'Creche'),
# 		('G1', 'Maternal I'),
# 		('G2', 'Maternal II'),
# 		('G3', 'Maternal III'),
# 		('G4', 'Jardim I'),
# 		('G5', 'Jardim II'),
# 		('1A', '1º Ano'),
# 		('2A', '2º Ano'),
# 		('3A', '3º Ano'),
# 		('4A', '4º Ano'),
# 		('5A', '5º Ano'),
# 		('6A', '6º Ano'),
# 		('7A', '7º Ano'),
# 		('8A', '8º Ano'),
# 		('9A', '9º Ano'),
# 	)
#
# 	ano_escolar_id = models.AutoField(primary_key=True)
# 	ano_escolar_nome = models.CharField(
# 		'Ano escolar',
# 		max_length=2,
# 		choices=ANO_ESCOLAR_CHOICES
# 	)
# 	ano_escolar_etapa = models.ForeignKey(
# 		EtapaBasica,
# 		on_delete=models.CASCADE,
# 		verbose_name='Etapa',
# 		related_name='anoescolaretapa'
# 	)
#
# 	class Meta:
# 		verbose_name = 'Ano Escolar'
# 		verbose_name_plural = 'Anos Escolares'
# 		constraints = [
# 			models.UniqueConstraint(
# 				fields=['ano_escolar_nome', 'ano_escolar_etapa'],
# 				name='unico_ano_escolar_na_etapa'
# 			)
# 		]
# 		ordering = ['ano_escolar_etapa', 'ano_escolar_nome']
#
# 	def __str__(self):
# 		return '{} - {}'.format(
# 			self.get_ano_escolar_nome_display(),
# 			self.ano_escolar_etapa
# 		)
