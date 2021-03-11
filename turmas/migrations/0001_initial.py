# Generated by Django 3.1.3 on 2021-03-09 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0001_initial'),
        ('principal', '0003_auto_20210306_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('turma_id', models.AutoField(primary_key=True, serialize=False)),
                ('turma_nome', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1, verbose_name='Nome')),
                ('turma_aluno', models.ManyToManyField(related_name='turmaaluno', to='alunos.Aluno', verbose_name='Alunos')),
                ('turma_ano_escolar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='turmaanoescolar', to='principal.anoescolar', verbose_name='Ano Escolar')),
                ('turma_disciplina', models.ManyToManyField(related_name='turmadisciplinas', to='principal.Disciplina', verbose_name='Disciplinas')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ['turma_ano_escolar', 'turma_nome'],
            },
        ),
        migrations.AddConstraint(
            model_name='turma',
            constraint=models.UniqueConstraint(fields=('turma_ano_escolar', 'turma_nome'), name='unica_turma_ano'),
        ),
    ]