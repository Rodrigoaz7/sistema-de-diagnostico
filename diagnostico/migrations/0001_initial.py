# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-28 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmentos', models.CharField(choices=[('Financeiro/Estrutural', 'Financeiro/Estrutural'), ('Marketing', 'Marketing'), ('Pessoas/Processos', 'Pessoas/Processos')], default='Financeiro/Estrutural', max_length=50)),
                ('nivel', models.IntegerField(verbose_name='Nivel (1, 2 ou 3)')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Relatório',
                'verbose_name_plural': 'Relatórios',
                'ordering': ['nivel'],
            },
        ),
    ]
