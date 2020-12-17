# Generated by Django 3.1.3 on 2020-12-17 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoFS',
            fields=[
                ('cfs_id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Código do Curso de Formação Superior')),
                ('cfs_nome_grau', models.CharField(max_length=100, unique=True, verbose_name='Nome do curso de Formação Superior')),
            ],
        ),
        migrations.AlterField(
            model_name='pais',
            name='pais_codigo',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, unique=True, verbose_name='Código do País'),
        ),
    ]
