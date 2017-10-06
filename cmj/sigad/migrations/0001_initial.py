# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-28 13:14
from __future__ import unicode_literals

import cmj.sigad.models
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields.json
from unipath import Path

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('parlamentares', '0001_initial'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('public_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Início de Publicação')),
                ('public_end_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Fim de Publicação')),
                ('descricao', models.TextField(blank=True, default=None, null=True, verbose_name='Descrição')),
                ('autor', models.TextField(blank=True, default=None, null=True, verbose_name='Autor')),
                ('visibilidade', models.IntegerField(choices=[(1, 'Restrito'), (99, 'Privado'), (0, 'Público')], default=99, verbose_name='Visibilidade')),
                ('titulo', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Título')),
                ('slug', models.SlugField(max_length=2000)),
                ('codigo', models.PositiveIntegerField(default=0, verbose_name='Código')),
                ('perfil', models.IntegerField(choices=[(0, 'Classe Estrutural'), (1, 'Classe de Conteúdo'), (2, 'Classe Mista')], default=0, verbose_name='Perfil da Classe')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='sigad.Classe', verbose_name='Filhos')),
                ('related_classes', models.ManyToManyField(blank=True, related_name='_classe_related_classes_+', to='sigad.Classe', verbose_name='Classes Relacionadas')),
            ],
            options={
                'verbose_name_plural': 'Classes',
                'permissions': (('view_subclasse', 'Visualização de Subclasses'),),
                'verbose_name': 'Classe',
                'ordering': ('codigo', '-public_date'),
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('public_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Início de Publicação')),
                ('public_end_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Fim de Publicação')),
                ('descricao', models.TextField(blank=True, default=None, null=True, verbose_name='Descrição')),
                ('autor', models.TextField(blank=True, default=None, null=True, verbose_name='Autor')),
                ('visibilidade', models.IntegerField(choices=[(1, 'Restrito'), (99, 'Privado'), (0, 'Público')], default=99, verbose_name='Visibilidade')),
                ('titulo', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Título')),
                ('slug', models.SlugField(max_length=2000)),
                ('texto', models.TextField(blank=True, default=None, null=True, verbose_name='Texto')),
                ('old_path', models.TextField(blank=True, default=None, null=True, verbose_name='Path no Portal Modelo 1.0')),
                ('old_json', models.TextField(blank=True, default=None, null=True, verbose_name='Json no Portal Modelo 1.0')),
                ('tipo', models.IntegerField(choices=[(100, 'Texto'), (800, 'Vídeo'), (900, 'Imagem')], default=0, verbose_name='Tipo da Parte do Documento')),
                ('ordem', models.IntegerField(default=0, verbose_name='Ordem de Renderização')),
                ('classe', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documento_set', to='sigad.Classe', verbose_name='Classes')),
                ('materias', models.ManyToManyField(related_name='documento_set', to='materia.MateriaLegislativa', verbose_name='Matérias Relacionadas')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='sigad.Documento', verbose_name='Filhos')),
                ('parlamentares', models.ManyToManyField(related_name='documento_set', to='parlamentares.Parlamentar', verbose_name='Parlamentares')),
                ('related_classes', models.ManyToManyField(blank=True, related_name='_documento_related_classes_+', to='sigad.Documento', verbose_name='Classes Relacionadas')),
            ],
            options={
                'verbose_name_plural': 'Documentos',
                'permissions': (('view_documento', 'Visualização dos Metadados do Documento.'), ('view_documento_media', 'Visualização das mídias do Documento')),
                'verbose_name': 'Documento',
                'ordering': ('public_date',),
            },
        ),
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='midia', to='sigad.Documento', verbose_name='Mídia')),
            ],
            options={
                'verbose_name_plural': 'Mídias Versionadas',
                'verbose_name': 'Mídia Versionada',
            },
        ),
        migrations.CreateModel(
            name='PermissionsUserClasse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('public_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Início de Publicação')),
                ('public_end_date', models.DateTimeField(default=None, null=True, verbose_name='Data de Fim de Publicação')),
                ('descricao', models.TextField(blank=True, default=None, null=True, verbose_name='Descrição')),
                ('autor', models.TextField(blank=True, default=None, null=True, verbose_name='Autor')),
                ('visibilidade', models.IntegerField(choices=[(1, 'Restrito'), (99, 'Privado'), (0, 'Público')], default=99, verbose_name='Visibilidade')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigad.Classe', verbose_name='Classe')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission', verbose_name='Permissão')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Permissões de Usuários para Classes',
                'verbose_name': 'Permissão de Usuário para Classe',
            },
        ),
        migrations.CreateModel(
            name='Revisao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('json', django_extensions.db.fields.json.JSONField(verbose_name='Json')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Revisões',
                'verbose_name': 'Revisão',
                'ordering': ('-data',),
            },
        ),
        migrations.CreateModel(
            name='VersaoDeMidia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('file', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='DO_NOT_USE', location=Path('/home/sapl31/cmj/media_protected')), upload_to=cmj.sigad.models.media_path, verbose_name='Mídia')),
                ('content_type', models.CharField(default='', max_length=250)),
                ('alinhamento', models.IntegerField(choices=[(0, 'Alinhamento Esquerdo'), (1, 'Alinhamento Completo'), (2, 'Alinhamento Direito')], default=0, verbose_name='Alinhamento')),
                ('midia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='sigad.Midia', verbose_name='Mídia Versionada')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name_plural': 'Mídias',
                'verbose_name': 'Mídia',
                'ordering': ('-created',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='permissionsuserclasse',
            unique_together=set([('user', 'classe', 'permission')]),
        ),
        migrations.AlterUniqueTogether(
            name='classe',
            unique_together=set([('slug', 'parent')]),
        ),
    ]