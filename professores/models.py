from django.db import models

from base import constants

from base.validators import (
	validate_digits,
	validate_no_digits,
	validate_data,
	validate_professor_inep,
	validate_cpf,
	validate_ddd,
	validate_phone,
	validate_cep,
	validate_year,
	)

from base.models import AreaConhecimento, CursoFS, Municipio, Pais


class Professor(models.Model):

	CHOICES_PROFESSOR_SITUACAO = (
		('0', 'Concursado'),
		('1', 'CLT'),
		('2', 'Temporário'),
		('3', 'Substituto'),
		('4', 'Estagiário'),
		('5', 'Terceirizado'),
		('6', 'Curriculo'),
		('7', 'Atestado'),
		('8', 'Demitido'),
	)

	CHOICES_PROFESSOR_JUSTIFICATIVA_DOCUMENTOS = (
		('1', 'O aluno(a) não possui os documentos solicitados'),
		('2', 'A escola não recebeu os documentos solicitados')
	)

	CHOICES_PROFESSOR_COR = (
		('0', 'Não declarada'),
		('1', 'Branca'),
		('2', 'Preta'),
		('3', 'Parda'),
		('4', 'Amarela'),
		('5', 'Indígena'),
	)

	CHOICES_PROFESSOR_SEXO = (
		('1', 'Masculino'),
		('2', 'Feminino')
	)

	CHOICES_PROFESSOR_NACIONALIDADE = (
		('1', 'Brasileira'),
		('2', 'Brasileira - Naturalizado(a)'),
		('3', 'Estrangeira'),
	)

	CHOICES_PROFESSOR_ESTADO = (
		('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
		('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
		('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
		('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
		('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'),
		('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
		('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
		('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
		('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'),
		('TO', 'Tocantins')
	)

	CHOICES_PROFESSOR_ZONA = (
		('1', 'Urbana'),
		('2', 'Rural')
	)

	CHOICES_PROFESSOR_ZONA_DIFERENCIADA = (
		('1', 'Área de assentamento'),
		('2', 'Terra indígena'),
		('3', 'Área quilombola'),
		('7', 'Não está em uma localização diferenciada')
	)

	CHOICES_FILIACAO = (
		('0', 'Não declarado/Ignorado'),
		('1', 'Filiação 1 e/ou Filiação 2')
	)

	CHOICES_SIM_NAO = (
		('0', 'Não'),
		('1', 'Sim')
	)

	CHOICES_ENSINO_OUTRO_LUGAR = (
		('1', 'Não'),
		('2', 'Hospital'),
		('3', 'Domicílio'),
		('4', 'Instalações exteriores')
	)

	CHOICES_NIVEL_ESCOLARIDADE = (
		('1', 'Não concluiu o ensino fundamental'),
		('2', 'Ensino fundamental'),
		('7', 'Ensino médio'),
		('6', 'Ensino superior')
	)

	CHOICES_TIPO_ENSINO_MEDIO = (
		('1', 'Formação geral'),
		('2', 'Modalidade normal (magistério)'),
		('3', 'Curso técnico'),
		('4', 'Magistério indígena, modalidade normal')
	)

	# --- End Choices constants --- #
	# use for person personal code in school
	professor_id = models.AutoField(
		primary_key=True
	)
	# --- OK --- #
	professor_situacao = models.CharField(
		'Situação do professor(a)',
		max_length=1,
		choices=CHOICES_PROFESSOR_SITUACAO
	)
	# --- professor Documentos --- #
	# --- OK MEC--- #
	# Need 12 digits
	professor_inep = models.CharField(
		'Inep',
		max_length=12,
		blank=True,
		null=True,
		unique=True,
		validators=[validate_professor_inep, validate_digits]
	)
	# --- OK MEC --- #
	# Need 11 digits
	professor_cpf = models.CharField(
		'Cpf',
		max_length=14,
		blank=True,
		null=True,
		unique=True,
		validators=[validate_cpf]
	)
	# --- OK --- #
	professor_rg = models.CharField(
		'RG',
		max_length=20,
		blank=True,
		null=True,
		unique=True
	)
	# --- professor Dados Pessoais --- #
	# --- OK MEC --- #
	professor_nome = models.CharField(
		'Nome completo',
		max_length=100,
		validators=[validate_no_digits]
	)
	# --- OK MEC --- #
	professor_data_nascimento = models.CharField(
		'Data de nascimento',
		max_length=10,
		validators=[validate_data]
	)
	# --- OK MEC --- #
	# Required - Accept 1 / 2
	professor_sexo = models.CharField(
		'Sexo',
		max_length=1,
		choices=CHOICES_PROFESSOR_SEXO,
	)
	# --- OK MEC --- #
	# Required - Accept 0 -> 5
	professor_cor = models.CharField(
		'Cor / Raça',
		max_length=1,
		choices=CHOICES_PROFESSOR_COR,
		default='0'
	)
	# --- professor Nacionalidade --- #
	# Required - Accept 1 -> 3
	# --- OK MEC --- #
	professor_nacionalidade = models.CharField(
		'Nacionalidade',
		max_length=1,
		choices=CHOICES_PROFESSOR_NACIONALIDADE,
		default='1'
	)
	# --- OK MEC --- #
	professor_pais_nascimento = models.ForeignKey(
		Pais,
		on_delete=models.DO_NOTHING,
		verbose_name='País de nascimento',
		related_name='professorpaisnascimento',
		default=constants.PAIS,
	)
	# --- OK --- #
	professor_estado_nascimento = models.CharField(
		'Estado',
		max_length=2,
		choices=CHOICES_PROFESSOR_ESTADO,
		blank=True,
	)
	# --- OK MEC --- #
	professor_municipio_nascimento = models.CharField(
		'Municipio nascimento',
		max_length=100,
		blank=True,
	)
	# professor_municipio_nascimento = models.ForeignKey(
	# 	Municipio,
	# 	on_delete=models.DO_NOTHING,
	# 	verbose_name='Município',
	# 	related_name='professormunicipionascimento',
	# 	blank=True,
	# 	null=True,
	# )
	# --- professor residencia --- #
	# --- OK --- #
	professor_logradouro_residencia = models.CharField(
		'Logradoro',
		max_length=100,
	)
	# --- OK --- #
	professor_numero_residencia = models.CharField(
		'Número',
		max_length=10,
	)
	# --- OK --- #
	professor_complemento_residencia = models.CharField(
		'Complemento',
		max_length=100,
		blank=True
	)
	# --- OK MEC --- #
	# Required - Accept 1 2
	professor_zona_residencia = models.CharField(
		'Localização',
		max_length=1,
		choices=CHOICES_PROFESSOR_ZONA,
		default='1'
	)
	# --- OK MEC --- #
	# Required - Accept 1 2 3 7
	professor_localizacao_residencia = models.CharField(
		'Localização diferenciada',
		max_length=1,
		choices=CHOICES_PROFESSOR_ZONA_DIFERENCIADA,
		default='7'
	)
	# --- OK --- #
	professor_bairro_residencia = models.CharField(
		'Bairro',
		max_length=50,
		blank=True
	)
	# --- OK MEC --- #
	professor_cep_residencia = models.CharField(
		'CEP',
		max_length=9,
		validators=[validate_cep],
	)
	# --- OK --- #
	professor_estado_residencia = models.CharField(
		'Estado',
		max_length=2,
		choices=CHOICES_PROFESSOR_ESTADO,
		default=constants.ESTADO
	)
	# --- OK MEC --- #
	professor_municipio_residencia = models.CharField(
		'Municipio residência',
		max_length=100,
	)
	# # Default for city school - first in cities table
	# professor_municipio_residencia = models.ForeignKey(
	# 	Municipio,
	# 	on_delete=models.DO_NOTHING,
	# 	verbose_name='Município',
	# 	related_name='professormunicipioresidencia',
	# 	default=MUNICIPIO
	# )
	# --- OK MEC --- #
	professor_pais_residencia = models.ForeignKey(
		Pais,
		on_delete=models.DO_NOTHING,
		verbose_name='País',
		related_name='professorpaisresidencia',
		default=constants.PAIS
	)
	# --- professor contacto --- #
	# --- OK --- #
	professor_ddd = models.CharField(
		'professor - DDD Telefone',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits],
	)
	# --- OK --- #
	professor_telefone = models.CharField(
		'professor - Telefone',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits],
	)
	# --- OK MEC --- #
	professor_email = models.EmailField(
		'Email',
		max_length=250,
		blank=True,
		null=True,
		unique=True
	)
	# --- professor filiação --- #
	# --- OK MEC --- #
	professor_filiacao = models.CharField(
		'Filiação',
		max_length=1,
		choices=CHOICES_FILIACAO
	)
	# --- professor filiação 1 --- #
	### --- OK MEC --- #
	professor_filiacao1_nome = models.CharField(
		'Filiação 1 - Nome',
		max_length=100,
		blank=True,
		validators=[validate_no_digits]
	)
	# --- professor filiação 2 --- #
	# --- OK MEC --- #
	professor_filiacao2_nome = models.CharField(
		'Filiação 2 - Nome',
		max_length=100,
		blank=True,
		validators=[validate_no_digits]
	)
	# --- Ensino em outro lugar --- #
	# --- OK --- #
	# 1 -> 4
	professor_ensino_outro_lugar = models.CharField(
		'Ensino em outro lugar',
		max_length=1,
		blank=True,
		choices=CHOICES_ENSINO_OUTRO_LUGAR,
		default='1'
	)
	# --- Escolaridade --- #
	# --- OK MEC --- #
	professor_nivel_escolaridade = models.CharField(
		'Maior nível de escolaridade',
		max_length=1,
		choices=CHOICES_NIVEL_ESCOLARIDADE
	)
	# --- OK MEC --- #
	professor_tipo_ensino_medio = models.CharField(
		'Tipo de ensino médio cursado',
		max_length=1,
		blank=True,
		choices=CHOICES_TIPO_ENSINO_MEDIO
	)
	# --- Cursos --- #
	# --- OK MEC --- #
	professor_curso1 = models.ForeignKey(
		CursoFS,
		on_delete=models.DO_NOTHING,
		verbose_name='Curso Formação Superior',
		related_name='professorcurso1',
		blank=True,
		null=True
	)
	# --- OK MEC --- #
	professor_curso_conclusao1 = models.CharField(
		'Ano de conclusão',
		max_length=4,
		blank=True,
		validators=[validate_year, validate_digits]
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_publica1 = models.CharField(
		'Pública',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_privada1 = models.CharField(
		'Privada',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# TODO will change for the institution number for use in MEC import
	professor_curso_instituicao1 = models.CharField(
		'Instituição de Educação Superior',
		max_length=100,
		blank=True,
	)
	# --- OK MEC --- #
	professor_curso2 = models.ForeignKey(
		CursoFS,
		on_delete=models.DO_NOTHING,
		verbose_name='Curso Formação Superior',
		related_name='professorcurso2',
		blank=True,
		null=True
	)
	# --- OK MEC --- #
	professor_curso_conclusao2 = models.CharField(
		'Ano de conclusão',
		max_length=4,
		blank=True,
		validators=[validate_year, validate_digits]
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_publica2 = models.CharField(
		'Pública',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_privada2 = models.CharField(
		'Privada',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# TODO Need the institution number for use in MEC import
	professor_curso_instituicao2 = models.CharField(
		'Instituição de Educação Superior',
		max_length=100,
		blank=True,
	)
	# --- OK MEC --- #
	professor_curso3 = models.ForeignKey(
		CursoFS,
		on_delete=models.DO_NOTHING,
		verbose_name='Curso Formação Superior',
		related_name='professorcurso3',
		blank=True,
		null=True
	)
	# --- OK MEC --- #
	professor_curso_conclusao3 = models.CharField(
		'Ano de conclusão',
		max_length=4,
		blank=True,
		validators=[validate_year, validate_digits]
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_publica3 = models.CharField(
		'Pública',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_privada3 = models.CharField(
		'Privada',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# TODO Need the institution number for use in MEC import
	professor_curso_instituicao3 = models.CharField(
		'Instituição de Educação Superior',
		max_length=100,
		blank=True,
	)
	# --- Formação / Complementação Pedagógica --- #
	professor_area_conhecimento1 = models.ForeignKey(
		AreaConhecimento,
		on_delete=models.DO_NOTHING,
		verbose_name='Componenete curricular',
		related_name='professorareaconhecimento1',
		blank=True,
		null=True
	)
	professor_area_conhecimento2 = models.ForeignKey(
		AreaConhecimento,
		on_delete=models.DO_NOTHING,
		verbose_name='Componenete curricular',
		related_name='professorareaconhecimento2',
		blank=True,
		null=True
	)
	professor_area_conhecimento3 = models.ForeignKey(
		AreaConhecimento,
		on_delete=models.DO_NOTHING,
		verbose_name='Componenete curricular',
		related_name='professorareaconhecimento3',
		blank=True,
		null=True
	)
	# --- Pós graduações concluidas --- #
	# 0 or 1
	professor_pos_graduacao_concluida = models.CharField(
		'Tem pós graduação concluida',
		max_length=1,
		choices=CHOICES_SIM_NAO
	)
	# --- OK MEC --- #
	# blank or 1
	professor_especializacao = models.CharField(
		'Especialização',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_mestrado = models.CharField(
		'Mestrado',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_doutorado = models.CharField(
		'Doutorado',
		max_length=1,
		blank=True
	)
	# --- Outros cursos específicos --- #
	# 0 or 1
	professor_outros_cursos = models.CharField(
		'Outros cursos específicos',
		max_length=1,
		choices=CHOICES_SIM_NAO
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_creche = models.CharField(
		'Creche',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_pre_escola = models.CharField(
		'Pré-escola',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_fundamental1 = models.CharField(
		'Anos iniciais do ensino fundamental',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_fundamental2 = models.CharField(
		'Anos finais do ensino fundamental',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_ensino_medio = models.CharField(
		'Ensino médio',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_educacao_especial = models.CharField(
		'Educação especial',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_jovens_adultos = models.CharField(
		'Educação de jovens e adultos',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_educacao_indigena = models.CharField(
		'Educação indígena',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_educacao_campo = models.CharField(
		'Educação do campo',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_educacao_ambiental = models.CharField(
		'Educação ambiental',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_direitos_humanos = models.CharField(
		'Educação em direitos humanos',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_diversidade_sexual = models.CharField(
		'Gênero e diversidade sexual',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_direitos_crianca = models.CharField(
		'Direitos de crianças e adolescentes',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_relacoes_etnicas = models.CharField(
		'Educação para as relações étnico-raciais',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_gestao_escolar = models.CharField(
		'Gestão escolar',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_curso_outros = models.CharField(
		'Outros cursos',
		max_length=1,
		blank=True
	)
	# --- OK --- #
	professor_justificativa_documentos = models.CharField(
		'Justificativa da falta de documentos',
		max_length=1,
		blank=True,
		choices=CHOICES_PROFESSOR_JUSTIFICATIVA_DOCUMENTOS
	)
	# --- professor deficiencias --- #
	# --- OK MEC --- #
	# 0 or 1
	professor_deficiencia = models.CharField(
		'Tem Deficiência Física',
		max_length=1,
		choices=CHOICES_SIM_NAO
	)
	# --- OK MEC --- #
	# blank or 1
	professor_cegueira = models.CharField(
		'Cegueira',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_baixa_visao = models.CharField(
		'Baixa visão',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_surdez = models.CharField(
		'Surdez',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_deficiencia_auditiva = models.CharField(
		'Deficiência auditiva',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_surdocegueira = models.CharField(
		'Surdocegueira',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_deficiencia_fisica = models.CharField(
		'Deficiência física',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_deficiencia_intelectual = models.CharField(
		'Deficiência intelectual',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_deficiencia_multipla = models.CharField(
		'Deficiência múltipla',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_autismo = models.CharField(
		'Autismo',
		max_length=1,
		blank=True
	)
	# --- OK MEC --- #
	# blank or 1
	professor_altas_habilidades = models.CharField(
		'Altas habilidades',
		max_length=1,
		blank=True
	)
	# --- Urgencia --- #
	# --- OK --- #
	professor_urgencia_nome = models.CharField(
		'Urgência - Nome',
		max_length=100,
		blank=True
	)
	# --- OK --- #
	professor_urgencia_ddd = models.CharField(
		'Urgência - DDD',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	# --- OK --- #
	professor_urgencia_telefone = models.CharField(
		'Urgência - Telefone',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	# --- OK --- #
	professor_urgencia_parentesco = models.CharField(
		'Urgência - Parentesco',
		max_length=50,
		blank=True
	)
	# --- OK --- #
	professor_urgencia_procedimentos = models.TextField(
		'Procedimentos em caso de urgência',
		blank=True
	)
	# --- professor cuidados diferenciados --- #
	# --- OK --- #
	# blank or 1
	professor_alergia = models.CharField(
		'alergia',
		max_length=1,
		blank=True
	)
	# --- OK --- #
	professor_alergia_tipo = models.TextField(
		'Tipo de alergia(s) e cuidados',
		max_length=1000,
		blank=True
	)
	# --- OK --- #
	professor_cuidados_diferenciados = models.TextField(
		'Cuidados diferenciados',
		max_length=1000,
		blank=True
	)
	# --- Plano de saude --- #
	# --- OK --- #
	# blank or 1
	professor_plano_saude = models.CharField(
		'Plano de Saúde',
		max_length=1,
		blank=True
	)
	# --- OK --- #
	professor_plano_saude_nome = models.CharField(
		'Nome do Plano de Saúde',
		max_length=50,
		blank=True
	)
	# --- OK --- #
	professor_plano_saude_ddd = models.CharField(
		'DDD',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	# --- OK --- #
	professor_plano_saude_telefone = models.CharField(
		'Telefone',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	# --- OK --- #
	professor_plano_saude_email = models.EmailField(
		'Email',
		max_length=250,
		blank=True,
	)
	# --- Convenio --- #
	# --- OK --- #
	# blank or 1
	professor_convenio = models.CharField(
		'Convênio',
		max_length=1,
		blank=True
	)
	# --- OK --- #
	professor_convenio_nome = models.CharField(
		'Nome do convênio',
		max_length=50,
		blank=True
	)
	# --- OK --- #
	professor_convenio_ddd = models.CharField(
		'DDD',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	# --- OK --- #
	professor_convenio_telefone = models.CharField(
		'Telefone',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	# --- OK --- #
	professor_convenio_email = models.EmailField(
		'Email',
		max_length=250,
		blank=True,
	)
	# --- Programa social --- #
	# --- OK --- #
	# blank or 1
	professor_programa_social = models.CharField(
		'Convênio',
		max_length=1,
		blank=True
	)
	# --- OK --- #
	professor_programa_social_nome = models.CharField(
		'Nome do convênio',
		max_length=50,
		blank=True
	)
	# --- OK --- #
	professor_programa_social_ddd = models.CharField(
		'DDD',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	# --- OK --- #
	professor_programa_social_telefone = models.CharField(
		'Telefone',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	# --- OK --- #
	professor_programa_social_email = models.EmailField(
		'Email',
		max_length=250,
		blank=True,
	)
	# --- Estagio --- #
	# --- OK --- #
	# blank or 1
	professor_estagio = models.CharField(
		'Estagio',
		max_length=1,
		blank=True
	)
	# --- OK --- #
	professor_estagio_instituicao = models.CharField(
		'Instituição',
		max_length=100,
		blank=True
	)
	# --- OK --- #
	professor_estagio_tempo = models.CharField(
		'Tempo',
		max_length=100,
		blank=True
	)
	# --- OK --- #
	professor_estagio_observacoes = models.TextField(
		'Observações sobre o estágio',
		max_length=1000,
		blank=True
	)
	# --- Observações --- #
	# --- OK --- #
	professor_observacoes = models.TextField(
		'Observações',
		max_length=1000,
		blank=True
	)
	# --- Data de criação ou modificação --- #
	created = models.DateTimeField('Data da Criação', auto_now_add=True)
	modified = models.DateTimeField('Data da alteração', auto_now=True)

	def professor_codigo_id(self):
		"""
		Return custom unique identification
		"""
		return 'pr-' + str(self.professor_id)

	class Meta:
		verbose_name = 'Professor'
		verbose_name_plural = 'Professores'
		ordering = ['professor_nome']

	def __str__(self):
		return self.professor_nome
