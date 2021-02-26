# Generated by Django 3.1.3 on 2021-02-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anoletivo',
            options={'ordering': ['-ano_letivo_nome'], 'verbose_name': 'Ano Letivo', 'verbose_name_plural': 'Anos Letivos'},
        ),
        migrations.AlterField(
            model_name='etapabasico',
            name='etapa_basico_ano',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.anoletivo', verbose_name='Ano Letivo'),
        ),
    ]