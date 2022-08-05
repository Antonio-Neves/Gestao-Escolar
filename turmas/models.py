from django.db import models
from base.constants import(
	HORA_INICIAL_MANHA,
	HORA_INICIAL_TARDE,
	HORA_FINAL_MANHA,
	HORA_FINAL_TARDE
)
from base.validators import validate_digits, validate_ano_letivo

from principal.models import Disciplina
from alunos.models import Aluno
from base.models import AtividadeComplementar


class Turma(models.Model):

	TURMA_NOME_CHOICES = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D')
	)
	TURMA_HORA_INICIAL_CHOICES = (
		(HORA_INICIAL_MANHA, HORA_INICIAL_MANHA),
		(HORA_INICIAL_TARDE, HORA_INICIAL_TARDE)
	)
	TURMA_HORA_FINAL_CHOICES = (
		(HORA_FINAL_MANHA, HORA_FINAL_MANHA),
		(HORA_FINAL_TARDE, HORA_FINAL_TARDE)
	)
	TURMA_MEDIACAO_PEDAGOGICA_CHOICES = (
		('1', 'Presencial'),
		('2', 'Semipresencial'),
		('3', 'Educação a distância')
	)
	TURMA_LOCAL_DIFERENCIADO_CHOICES = (
		('0', 'Não está em local diferenciado'),
		('1', 'Sala anexa'),
		('2', 'Unidade de atendimento socioeducativa'),
		('3', 'Unidade Prisional')
	)
	TURMA_MODALIDADE_CHOICES = (
		('1', 'Ensino regular'),
		('2', 'Educação especial'),
		('3', 'Educação de jovens e adultos (EJA)'),
		('4', 'Educação profissional')
	)
	TURMA_ANO_ESCOLAR_CHOICES = (
		('CR', 'Creche'),
		('G1', 'Maternal I'),
		('G2', 'Maternal II'),
		('G3', 'Maternal III'),
		('G4', 'Jardim I'),
		('G5', 'Jardim II'),
		('1A', '1º Ano'),
		('2A', '2º Ano'),
		('3A', '3º Ano'),
		('4A', '4º Ano'),
		('5A', '5º Ano'),
		('6A', '6º Ano'),
		('7A', '7º Ano'),
		('8A', '8º Ano'),
		('9A', '9º Ano'),
	)
	TURMA_ETAPA_BASICA_CHOICES = (
		('IN', 'Infantil'),
		('F1', 'Fundamental I'),
		('F2', 'Fundamental II'),
		('EM', 'Ensino Médio')
	)
	# --- End Turma choices --- #

	# --- Turma fields --- #
	turma_id = models.AutoField(
		primary_key=True
	)
	turma_ano_escolar = models.CharField(
		'Ano Escolar',
		max_length=2,
		choices=TURMA_ANO_ESCOLAR_CHOICES
	)
	turma_nome = models.CharField(
		'Nome',
		max_length=1,
		choices=TURMA_NOME_CHOICES,
		default='A'
	)
	# -----------------------------
	# TODO Change 'turma_etapa_basica' field with aux table if not 'Ensino Regular.
	# -----------------------------
	turma_etapa_basica = models.CharField(
		'Etapa Básica',
		max_length=2,
		choices=TURMA_ETAPA_BASICA_CHOICES
	)
	turma_ano_letivo = models.CharField(
		'Ano Letivo',
		max_length=4,
		validators=[validate_digits, validate_ano_letivo]
	)
	# TODO 'alunos'
	turma_aluno = models.ManyToManyField(
		Aluno,
		verbose_name='Alunos',
		related_name='turmaaluno'
	)
	# TODO 'disciplinas'
	turma_disciplina = models.ManyToManyField(
		Disciplina,
		verbose_name='Disciplinas',
		related_name='turmadisciplinas'
	)
	# --- Mediação didático-pedagógica
	turma_mediacao_pedagogica = models.CharField(
		'Mediação didático-pedagógica',
		max_length=2,
		choices=TURMA_MEDIACAO_PEDAGOGICA_CHOICES,
		default='1'
	)
	# --- Date time operation
	# Mec separa hora e minuto
	turma_hora_inicial = models.CharField(
		'Hora Inicial',
		max_length=5,
		choices=TURMA_HORA_INICIAL_CHOICES
	)
	# Mec separa hora e minuto
	turma_hora_final = models.CharField(
		'Hora final',
		max_length=5,
		choices=TURMA_HORA_FINAL_CHOICES
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_segunda = models.CharField(
		'Segunda',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_terca = models.CharField(
		'Terça',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_quarta = models.CharField(
		'Quarta',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_quinta = models.CharField(
		'Quinta',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_sexta = models.CharField(
		'Sexta',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_sabado = models.CharField(
		'Sábado',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_domingo = models.CharField(
		'Domingo',
		max_length=1,
		blank=True,
		null=True
	)
	# --- Type of service --- #
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_escolarizacao = models.CharField(
		'Escolarizacao',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_atividade_complementar = models.CharField(
		'Atividade complementar',
		max_length=1,
		blank=True,
		null=True
	)
	# TODO - checkbox field
	# only 0 no /1 yes values
	turma_atendimento_especializado = models.CharField(
		'Atendimento educacional specializado',
		max_length=1,
		blank=True,
		null=True
	)
	# --- 'atividade complementar' type --- #
	turma_atividade_complementar_codigo_1 = models.ForeignKey(
		AtividadeComplementar,
		verbose_name='Atividade complementar código 1',
		blank=True,
		null=True,
		on_delete=models.SET_NULL,
		related_name='atividadecomplementarcodigo1'
	)
	turma_atividade_complementar_codigo_2 = models.ForeignKey(
		AtividadeComplementar,
		verbose_name='Atividade complementar código 2',
		blank=True,
		null=True,
		on_delete=models.SET_NULL,
		related_name='atividadecomplementarcodigo2'
	)
	turma_atividade_complementar_codigo_3 = models.ForeignKey(
		AtividadeComplementar,
		verbose_name='Atividade complementar código 3',
		blank=True,
		null=True,
		on_delete=models.SET_NULL,
		related_name='atividadecomplementarcodigo3'
	)
	turma_atividade_complementar_codigo_4 = models.ForeignKey(
		AtividadeComplementar,
		verbose_name='Atividade complementar código 4',
		blank=True,
		null=True,
		on_delete=models.SET_NULL,
		related_name='atividadecomplementarcodigo4'
	)
	turma_atividade_complementar_codigo_5 = models.ForeignKey(
		AtividadeComplementar,
		verbose_name='Atividade complementar código 5',
		blank=True,
		null=True,
		on_delete=models.SET_NULL,
		related_name='atividadecomplementarcodigo5'
	)
	turma_atividade_complementar_codigo_6 = models.ForeignKey(
		AtividadeComplementar,
		verbose_name='Atividade complementar código 6',
		blank=True,
		null=True,
		on_delete=models.SET_NULL,
		related_name='atividadecomplementarcodigo6'
	)
	turma_local_diferenciado = models.CharField(
		'Local de funcionamento diferenciado',
		max_length=1,
		choices=TURMA_LOCAL_DIFERENCIADO_CHOICES,
		default='0'
	)
	turma_modalidade = models.CharField(
		'Modalidade',
		max_length=1,
		choices=TURMA_MODALIDADE_CHOICES,
		default=1
	)
	# -----------------------------
	# TODO Create 'codigo_curso' field whit code if not 'ensino regular'.
	# -----------------------------

	# --- specials attributes --- #
	def turma_codigo_id(self):
		"""
		Return custom unique identification
		"""
		return 'turma-' + str(self.turma_id)

	def turma_nome_completo(self):
		"""
		Return complete 'Turma' name
		"""
		ano_escolar = self.get_turma_ano_escolar_display()
		nome = self.turma_nome
		etapa = self.turma_etapa_basica
		ano_letivo = self.turma_ano_letivo

		return f'{ano_escolar} {nome} - {etapa} {ano_letivo}'

	def turma_nome_etapa(self):
		"""
		Return 'Turma' minimal name with 'Etapa'
		"""
		ano_escolar = self.get_turma_ano_escolar_display()
		nome = self.turma_nome
		turma_etapa = self.turma_etapa_basica

		return f'{ano_escolar} {nome} - {turma_etapa}'

	class Meta:
		verbose_name = 'Turma'
		verbose_name_plural = 'Turmas'
		constraints = [
			models.UniqueConstraint(
				fields=['turma_ano_escolar', 'turma_nome', 'turma_ano_letivo'],
				name='unica_turma_ano'
			)
		]
		ordering = ['-turma_ano_letivo', 'turma_ano_escolar', 'turma_nome']

	def __str__(self):
		return self.turma_nome_completo()
