from django.db import models
from base.constants import (
	DDD,
	ESTADO,
	MUNICIPIO,
	CEP,
	PAIS,
)
from base.validators import (
	validate_digits,
	validate_no_digits,
	validate_data_nasc,
	validate_aluno_inep,
	validate_cpf,
	validate_ddd,
	validate_phone,
	validate_cep,
	validate_nis,
	validate_certidao_nascimento,
	)

from base.models import Municipio, Pais


# class Base(models.Model):
# 	created = models.DateTimeField('Data da Criação', auto_now_add=True)
# 	modified = models.DateTimeField('Data da alteração', auto_now=True)
#
# 	class Meta:
# 		abstract = True


class Aluno(models.Model):

	CHOICES_ALUNO_SITUACAO = (
		('A', 'Ativo'),
		('I', 'Inativo'),
		('T', 'Transferido'),
		('C', 'Cancelado'),
		('D', 'Desistente'),
		('F', 'Falecido'),
		('R', 'Remanejado')
	)

	CHOICES_ALUNO_JUSTIFICATIVA_DOCUMENTOS = (
		('1', 'O aluno(a) não possui os documentos solicitados'),
		('2', 'A escola não recebeu os documentos solicitados')
	)

	CHOICES_ALUNO_SEXO = (
		('1', 'Masculino'),
		('2', 'Feminino')
	)

	CHOICES_ALUNO_COR = (
		('0', 'Não declarada'),
		('1', 'Branca'),
		('2', 'Preta'),
		('3', 'Parda'),
		('4', 'Amarela'),
		('5', 'Indígena'),
	)

	CHOICES_ALUNO_NACIONALIDADE = (
		('1', 'Brasileira'),
		('2', 'Brasileira - Naturalizado(a)'),
		('3', 'Estrangeira'),
	)

	CHOICES_ALUNO_ESTADO = (
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

	CHOICES_ALUNO_ZONA = (
		('1', 'Urbana'),
		('2', 'Rural')
	)

	CHOICES_ALUNO_ZONA_DIFERENCIADA = (
		('1', 'Área de assentamento'),
		('2', 'Terra indígena'),
		('3', 'Área quilombola'),
		('7', 'Não está em uma localização diferenciada')
	)
	CHOICES_PODER_RESPONSAVEL_TRANSPORTE = (
		('1', 'Estadual'),
		('2', 'Municipal')
	)
	# --- End Choices constants --- #

	# use for person personal code in school
	aluno_id = models.AutoField(
		primary_key=True
	)
	# --- OK --- #
	aluno_situacao = models.CharField(
		'Situação do aluno(a)',
		max_length=1,
		choices=CHOICES_ALUNO_SITUACAO
	)
	# --- Aluno Documentos --- #
	# --- OK MEC--- #
	# Need 12 digits
	aluno_inep = models.CharField(
		'Inep',
		max_length=12,
		blank=True,
		null=True,
		unique=True,
		validators=[validate_aluno_inep, validate_digits]
	)
	# --- OK MEC --- #
	# Need 11 digits
	aluno_cpf = models.CharField(
		'Cpf',
		max_length=14,
		blank=True,
		null=True,
		unique=True,
		validators=[validate_cpf]
	)
	# --- OK --- #
	aluno_rg = models.CharField(
		'RG',
		max_length=20,
		blank=True,
		null=True,
		unique=True
	)
	# --- OK MEC --- #
	# Need 11 digits
	aluno_nis = models.CharField(
		'NIS',
		max_length=11,
		blank=True,
		null=True,
		unique=True,
		validators=[validate_nis, validate_digits]
	)
	# --- OK MEC --- #
	# Need 32 digits
	aluno_certidao_nova = models.CharField(
		'Certidão de nascimento - nova',
		max_length=40,
		validators=[validate_certidao_nascimento],
		blank=True,
		null=True,
		unique=True
	)
	# --- OK MEC --- #
	aluno_justificativa_documentos = models.CharField(
		'Justificativa da falta de documentos',
		max_length=1,
		blank=True,
		choices=CHOICES_ALUNO_JUSTIFICATIVA_DOCUMENTOS
	)
	# --- Aluno Dados Pessoais --- #
	# --- OK MEC --- #
	aluno_nome = models.CharField(
		'Nome completo',
		max_length=100,
		validators=[validate_no_digits]
	)
	# --- OK MEC --- #
	aluno_data_nascimento = models.DateField(
		'Data de nascimento',
		max_length=10,
		validators=[validate_data_nasc]
	)
	# --- OK MEC --- #
	# Required - Accept 1 / 2
	aluno_sexo = models.CharField(
		'Sexo',
		max_length=1,
		choices=CHOICES_ALUNO_SEXO,
	)
	# --- OK MEC --- #
	# Required - Accept 0 -> 5
	aluno_cor = models.CharField(
		'Cor / Raça',
		max_length=1,
		choices=CHOICES_ALUNO_COR,
		default='0'
	)
	# --- Aluno Nacionalidade --- #
	# Required - Accept 1 -> 3
	# --- OK MEC --- #
	aluno_nacionalidade = models.CharField(
		'Nacionalidade',
		max_length=1,
		choices=CHOICES_ALUNO_NACIONALIDADE,
		default='1'
	)
	# --- OK MEC --- #
	aluno_pais_nascimento = models.ForeignKey(
		Pais,
		on_delete=models.DO_NOTHING,
		verbose_name='País de nascimento',
		related_name='alunopaisnascimento',
		default=PAIS,
	)
	# --- OK --- #
	aluno_estado_nascimento = models.CharField(
		'Estado',
		max_length=2,
		choices=CHOICES_ALUNO_ESTADO,
		blank=True,
	)
	# --- OK MEC --- #
	aluno_municipio_nascimento = models.CharField(
		'Municipio nascimento',
		max_length=100,
		blank=True,
	)
	# aluno_municipio_nascimento = models.ForeignKey(
	# 	Municipio,
	# 	on_delete=models.DO_NOTHING,
	# 	verbose_name='Município',
	# 	related_name='alunomunicipionascimento',
	# 	blank=True,
	# 	null=True
	# )
	# --- Aluno residencia --- #
	# --- OK --- #
	aluno_logradouro_residencia = models.CharField(
		'Logradoro',
		max_length=100,
	)
	# --- OK --- #
	aluno_numero_residencia = models.CharField(
		'Número',
		max_length=10,
	)
	# --- OK --- #
	aluno_complemento_residencia = models.CharField(
		'Complemento',
		max_length=100,
		blank=True
	)
	# --- OK MEC --- #
	# Required - Accept 1 2
	aluno_zona_residencia = models.CharField(
		'Localização',
		max_length=1,
		choices=CHOICES_ALUNO_ZONA,
		default='1'
	)
	# --- OK MEC --- #
	# Required - Accept 1 2 3 7
	aluno_localizacao_residencia = models.CharField(
		'Localização diferenciada',
		max_length=1,
		choices=CHOICES_ALUNO_ZONA_DIFERENCIADA,
		default='7'
	)
	# --- OK --- #
	aluno_bairro_residencia = models.CharField(
		'Bairro',
		max_length=50,
		blank=True
	)
	# --- OK MEC --- #
	aluno_cep_residencia = models.CharField(
		'CEP',
		max_length=9,
		validators=[validate_cep],
	)
	# --- OK --- #
	aluno_estado_residencia = models.CharField(
		'Estado',
		max_length=2,
		choices=CHOICES_ALUNO_ESTADO,
		default=ESTADO
	)
	# --- OK MEC --- #
	aluno_municipio_residencia = models.CharField(
		'Municipio residência',
		max_length=100,
	)
	# # Default for city school - first in cities table
	# aluno_municipio_residencia = models.ForeignKey(
	# 	Municipio,
	# 	on_delete=models.DO_NOTHING,
	# 	verbose_name='Município',
	# 	related_name='alunomunicipioresidencia',
	# 	default=MUNICIPIO
	# )
	# --- OK MEC --- #
	aluno_pais_residencia = models.ForeignKey(
		Pais,
		on_delete=models.DO_NOTHING,
		verbose_name='País',
		related_name='alunopaisresidencia',
		default=PAIS
	)
	# --- Aluno contacto --- #
	# --- OK --- #
	aluno_ddd = models.CharField(
		'Aluno - DDD Telefone',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits],
	)
	# --- OK --- #
	aluno_telefone = models.CharField(
		'aluno - Telefone',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits],
	)
	# --- OK MEC --- #
	aluno_email = models.EmailField(
		'Email',
		max_length=250,
		blank=True,
		null=True,
		unique=True
	)
	# --- Aluno filiação --- #
	# TODO radio field Html
	# Required - Accept 0 / 1
	aluno_filiacao = models.CharField(
		'Filiação',
		max_length=1,
	)
	# --- Aluno filiação 1 --- #
	# TODO put (preferencialmente o nome da mãe) in Html
	aluno_filiacao1_nome = models.CharField(
		'Filiação 1 - Nome',
		max_length=100,
		blank=True,
		validators=[validate_no_digits]
	)
	# TODO need mask
	# Need 11 digits
	aluno_filiacao1_cpf = models.CharField(
		'Filiação 1 - Cpf',
		max_length=14,
		blank=True,
		validators=[validate_cpf]
	)
	aluno_filiacao1_rg = models.CharField(
		'Filiação 1 - RG',
		max_length=20,
		blank=True,
	)
	aluno_filiacao1_ddd1 = models.CharField(
		'Filiação 1 - DDD Telefone 1',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	aluno_filiacao1_telefone1 = models.CharField(
		'Filiação 1 - Telefone 1',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	aluno_filiacao1_ddd2 = models.CharField(
		'Filiação 1 - DDD Telefone 2',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	aluno_filiacao1_telefone2 = models.CharField(
		'Filiação 1 - Telefone 2',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	aluno_filiacao1_email = models.EmailField(
		'Filiação 1 - Email',
		max_length=250,
		blank=True,
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao1_respon_didatico = models.CharField(
		'Filiação 1 - Responsável didático',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao1_respon_financeiro = models.CharField(
		'Filiação 1 - Responsável financeiro',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao1_respon_legal = models.CharField(
		'Filiação 1 - Responsável legal',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao1_doc_guarda = models.CharField(
		'Filiação 1 - Documento da guarda',
		max_length=1,
		blank=True
	)
	aluno_filiacao1_parentesco = models.CharField(
		'Filiação 1 - Parentesco',
		max_length=50,
		blank=True
	)
	# --- Aluno filiação 2 --- #
	aluno_filiacao2_nome = models.CharField(
		'Filiação 2 - Nome',
		max_length=100,
		blank=True,
		validators=[validate_no_digits]
	)
	# TODO need mask
	# Need 11 digits
	aluno_filiacao2_cpf = models.CharField(
		'Filiação 2 - Cpf',
		max_length=14,
		blank=True,
		validators=[validate_cpf]
	)
	aluno_filiacao2_rg = models.CharField(
		'Filiação 2 - RG',
		max_length=20,
		blank=True,
	)
	aluno_filiacao2_ddd1 = models.CharField(
		'Filiação 2 - DDD Telefone 1',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	aluno_filiacao2_telefone1 = models.CharField(
		'Filiação 2 - Telefone 1',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	aluno_filiacao2_ddd2 = models.CharField(
		'Filiação 2 - DDD Telefone 2',
		max_length=2,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	aluno_filiacao2_telefone2 = models.CharField(
		'Filiação 2 - Telefone 2',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	aluno_filiacao2_email = models.EmailField(
		'Filiação 2 - Email',
		max_length=250,
		blank=True,
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao2_respon_didatico = models.CharField(
		'Filiação 2 - Responsável didático',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao2_respon_financeiro = models.CharField(
		'Filiação 2 - Responsável financeiro',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao2_respon_legal = models.CharField(
		'Filiação 2 - Responsável legal',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or '1'
	aluno_filiacao2_doc_guarda = models.CharField(
		'Filiação 2 - Documento da guarda',
		max_length=1,
		blank=True
	)
	aluno_filiacao2_parentesco = models.CharField(
		'Filiação 2 - Parentesco',
		max_length=50,
		blank=True
	)
	# --- Aluno deficiencias --- #
	# TODO radio field Html
	# 0 or 1
	aluno_deficiencia = models.CharField(
		'Tem Deficiência Física',
		max_length=1
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_cegueira = models.CharField(
		'Cegueira',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_baixa_visao = models.CharField(
		'Baixa visão',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_surdez = models.CharField(
		'Surdez',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_deficiencia_auditiva = models.CharField(
		'Deficiência auditiva',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_surdocegueira = models.CharField(
		'Surdocegueira',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_deficiencia_fisica = models.CharField(
		'Deficiência física',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_deficiencia_intelectual = models.CharField(
		'Deficiência intelectual',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_deficiencia_multipla = models.CharField(
		'Deficiência múltipla',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_autismo = models.CharField(
		'Autismo',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_altas_habilidades = models.CharField(
		'Altas habilidades',
		max_length=1,
		blank=True
	)
	# --- Aluno Necessidades Especiais
	# TODO check field Html value 1
	# blank or 1
	aluno_nenhuma_necessidade = models.CharField(
		'Nenhuma necessidade especial',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_auxilio_ledor = models.CharField(
		'Auxílio ledor',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_auxilio_transcricao = models.CharField(
		'Auxílio transcrição',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_guia_interprete = models.CharField(
		'Guia Intérprete',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_tradutor_libras = models.CharField(
		'Tradutor libras',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_leitura_labial = models.CharField(
		'Leitura labial',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_prova_ampliada18 = models.CharField(
		'Prova ampliada (fonte 18)',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_prova_superampliada24 = models.CharField(
		'Prova ampliada (fonte 24)',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_cd_audio = models.CharField(
		'Cd áudio',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_prova_portuguesa = models.CharField(
		'Prova de língua portuguesa',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_prova_video = models.CharField(
		'Prova em vídeo em libras',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_prova_braille = models.CharField(
		'Material e Prova em Braille',
		max_length=1,
		blank=True
	)
	# --- Aluno Necessidades diferenciadas
	# TODO check field Html value 1
	# blank or 1
	aluno_alergia = models.CharField(
		'alergia',
		max_length=1,
		blank=True
	)
	aluno_alergia_tipo = models.CharField(
		'Tipo de alergia',
		max_length=50,
		blank=True
	)
	aluno_alergia_cuidados = models.CharField(
		'Alergia cuidados',
		max_length=50,
		blank=True
	)
	# TODO check field Html value 1 default
	# blank or 1
	aluno_apto_edfisica = models.CharField(
		'alergia',
		max_length=1,
		blank=True
	)
	# --- convenio e programas sociais
	# TODO check field Html value 1
	# blank or 1
	aluno_convenio = models.CharField(
		'convenio',
		max_length=1,
		blank=True
	)
	aluno_convenio_nome = models.CharField(
		'Nome do convenio',
		max_length=50,
		blank=True
	)
	aluno_convenio_contato = models.CharField(
		'Contato do convenio',
		max_length=50,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_progrma_social = models.CharField(
		'Programa social',
		max_length=1,
		blank=True
	)
	aluno_programa_social_nome = models.CharField(
		'Nome do programa social',
		max_length=50,
		blank=True
	)
	# --- emergencia
	aluno_emergencia_nome = models.CharField(
		'Emergencia nome',
		max_length=100,
		blank=True
	)
	aluno_emergencia_ddd = models.CharField(
		'Emergencia DDD Telefone',
		max_length=2,
		default=DDD,
		blank=True,
		validators=[validate_ddd, validate_digits]
	)
	aluno_emergencia_telefone = models.CharField(
		'Emergencia telefone',
		max_length=9,
		blank=True,
		validators=[validate_phone, validate_digits]
	)
	aluno_emergencia_parentesco = models.CharField(
		'Emergencia parentesco',
		max_length=50,
		blank=True
	)
	# --- Saida escola
	# TODO check field Html value 1 (sozinho)
	# blank or 1
	aluno_saida_escola = models.CharField(
		'Saída da escola',
		max_length=1,
		blank=True
	)
	# TODO radio field Html value 1 (sozinho)
	# 1 -> 3
	aluno_ensino_outro_lugar = models.CharField(
		'Ensino em outro lugar',
		max_length=1,
		blank=True
	)
	# --- Transporte
	# TODO check field Html value 1
	# blank or 1
	aluno_transporte_publico = models.CharField(
		'Transporte Público',
		max_length=1,
		blank=True
	)
	# 1 or 2
	aluno_transporte_poder = models.CharField(
		'Poder responsavél pelo transporte público',
		max_length=1,
		blank=True,
		choices=CHOICES_PODER_RESPONSAVEL_TRANSPORTE
	)
	# --- Transporte rodoviario
	# TODO check field Html value 1
	# blank or 1
	aluno_rodoviario_particular = models.CharField(
		'Particular',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_rodoviario_bicicleta = models.CharField(
		'Bicicleta',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_rodoviario_microonibus = models.CharField(
		'Microonibus',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_rodoviario_onibus = models.CharField(
		'Onibus',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_rodoviario_animal = models.CharField(
		'Animal',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_rodoviario_van = models.CharField(
		'Van',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_rodoviario_outro = models.CharField(
		'Outro',
		max_length=1,
		blank=True
	)
	# --- Transporte Aquaviário
	# TODO check field Html value 1
	# blank or 1
	aluno_aquaviario_outro = models.CharField(
		'Particular',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_aquaviario_5 = models.CharField(
		'5 lugares',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_aquaviario_15 = models.CharField(
		'15 lugares',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_aquaviario_35 = models.CharField(
		'35 lugares',
		max_length=1,
		blank=True
	)
	# TODO check field Html value 1
	# blank or 1
	aluno_aquaviario_mais35 = models.CharField(
		'Mais de 35 lugares',
		max_length=1,
		blank=True
	)
	created = models.DateTimeField('Data da Criação', auto_now_add=True)
	modified = models.DateTimeField('Data da alteração', auto_now=True)
