# Generated by Django 3.1.2 on 2021-06-07 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='turma_atendimento_especializado',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Atendimento educacional specializado'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='turma_atividade_complementar',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Atividade complementar'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='turma_escolarizacao',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Escolarizacao'),
        ),
    ]
