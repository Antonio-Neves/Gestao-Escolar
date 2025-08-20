from django.core.management.base import BaseCommand
import pandas as pd
from principal.models import (
    AreaConhecimento, AtividadeComplementar, CursoFormacaoSuperior,
    Municipio, Pais, TipoAtividadeComplementar
)

class Command(BaseCommand):
    help = 'Importa dados dos arquivos Excel para o banco de dados'

    def handle(self, *args, **kwargs):
        base_path = 'notes_and_extras/Tabelas necessárias - Gestão Escolar/'

        def importar_excel(nome_arquivo, model, col_nome, col_codigo):
            try:
                df = pd.read_excel(base_path + nome_arquivo)
                for _, row in df.iterrows():
                    model.objects.get_or_create(
                        codigo=row[col_codigo],
                        defaults={'nome': row[col_nome]}
                    )
                self.stdout.write(self.style.SUCCESS(f'Dados importados: {model.__name__}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Erro ao importar {model.__name__}: {e}'))

        importar_excel('Tabela de Áreas do Conhecimento.xlsx', AreaConhecimento, 'nome_area', 'codigo_area')
        importar_excel('Tabela de Cursos de Formação Superior.xlsx', CursoFormacaoSuperior, 'nome', 'codigo')
        importar_excel('Tabela de Municípios.xlsx', Municipio, 'nome', 'codigo')
        importar_excel('Tabela de Países.xlsx', Pais, 'nome', 'codigo')
        importar_excel('Tabela de Tipo de Atividade Complementar.xlsx', TipoAtividadeComplementar, 'nome', 'codigo')