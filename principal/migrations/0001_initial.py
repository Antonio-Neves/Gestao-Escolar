# Generated by Django 3.1.2 on 2021-07-14 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina_nome', models.CharField(choices=[('port', 'Português'), ('ingl', 'Inglês'), ('espa', 'Espanhol'), ('mate', 'Matemática'), ('cien', 'Ciências'), ('hist', 'História'), ('arte', 'Artes'), ('geog', 'Geografia'), ('filo', 'Filosofia'), ('edfi', 'Educação Física'), ('enre', 'Ensino Religioso')], max_length=20, verbose_name='Disciplina')),
                ('disciplina_professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disciplinaprofessor', to='professores.professor', verbose_name='Professor(a)')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
                'ordering': ['disciplina_nome', 'disciplina_professor'],
            },
        ),
        migrations.AddConstraint(
            model_name='disciplina',
            constraint=models.UniqueConstraint(fields=('disciplina_nome', 'disciplina_professor'), name='unica_disciplina_professor'),
        ),
    ]
