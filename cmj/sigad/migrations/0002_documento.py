# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-07 16:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0036_partido_logo_partido'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sigad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('public_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Início de Publicação')),
                ('public_end_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Fim de Publicação')),
                ('descricao', models.TextField(blank=True, default=None, null=True, verbose_name='Descrição')),
                ('visibilidade', models.IntegerField(choices=[(1, 'Restrito'), (99, 'Privado'), (0, 'Público')], default=99, verbose_name='Visibilidade')),
                ('titulo', models.CharField(max_length=250, verbose_name='Título')),
                ('slug', models.SlugField(max_length=2000)),
                ('texto', models.TextField(blank=True, default=None, null=True, verbose_name='Texto')),
                ('old_id', models.TextField(blank=True, default=None, null=True, verbose_name='Id no Portal Modelo 1.0')),
                ('old_json', models.TextField(blank=True, default=None, null=True, verbose_name='Json no Portal Modelo 1.0')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='sigad.Classe', verbose_name='Classes')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='sigad.Documento', verbose_name='Filhos')),
                ('parlamentares', models.ManyToManyField(related_name='documentos', to='parlamentares.Parlamentar', verbose_name='Parlamentares')),
                ('related_classes', models.ManyToManyField(blank=True, related_name='_documento_related_classes_+', to='sigad.Documento', verbose_name='Classes Relacionadas')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'permissions': (('view_documento', 'Visualização dos Metadados do Documento.'), ('view_documento_media', 'Visualização das mídias do Documento')),
            },
        ),
    ]
