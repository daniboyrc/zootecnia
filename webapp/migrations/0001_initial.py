# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 02:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimaisCol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AnimaisEnum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('peso_nasc', models.FloatField()),
                ('peso_desm', models.FloatField()),
                ('pai', models.IntegerField()),
                ('mae', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividade', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(max_length=255)),
                ('reprodutor', models.IntegerField()),
                ('matriz', models.IntegerField()),
                ('data', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Evolucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evolucao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Leite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manha', models.FloatField()),
                ('tarde', models.FloatField()),
                ('total', models.FloatField(blank=True)),
                ('data', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='OcorAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.date.today)),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Atividade')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocorrencia', models.TextField()),
                ('data', models.DateField(default=datetime.date.today)),
                ('tratamento', models.TextField()),
                ('custo', models.FloatField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.AnimaisEnum')),
            ],
        ),
        migrations.CreateModel(
            name='Parto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_crias', models.IntegerField()),
                ('reprodutor', models.IntegerField()),
                ('data', models.DateField(default=datetime.date.today)),
                ('matriz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.AnimaisEnum')),
            ],
        ),
        migrations.CreateModel(
            name='Perda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causa', models.CharField(max_length=255)),
                ('data', models.DateField(default=datetime.date.today)),
                ('idade', models.IntegerField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.AnimaisEnum')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('proprietario', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('tamanho', models.IntegerField()),
                ('observacoes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEnum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.FloatField()),
                ('quantidade', models.FloatField()),
                ('data', models.DateField(default=datetime.date.today)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='animaisenum',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Estado'),
        ),
        migrations.AddField(
            model_name='animaisenum',
            name='evolucao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Evolucao'),
        ),
        migrations.AddField(
            model_name='animaisenum',
            name='propriedade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Propriedade'),
        ),
        migrations.AddField(
            model_name='animaisenum',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Raca'),
        ),
        migrations.AddField(
            model_name='animaisenum',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Sexo'),
        ),
        migrations.AddField(
            model_name='animaisenum',
            name='tipo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.TipoEnum'),
        ),
        migrations.AddField(
            model_name='animaiscol',
            name='propriedade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Propriedade'),
        ),
        migrations.AddField(
            model_name='animaiscol',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Raca'),
        ),
        migrations.AddField(
            model_name='animaiscol',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.TipoCol'),
        ),
    ]
