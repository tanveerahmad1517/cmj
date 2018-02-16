# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-15 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigad', '0033_auto_20180207_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='capa',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, help_text='Só um objeto pode ser capa de sua classe. Caso haja outro já selecionado, ele será desconsiderado.', verbose_name='Capa de sua Classe'),
        ),
        migrations.AlterField(
            model_name='classe',
            name='template_classe',
            field=models.IntegerField(choices=[(1, 'Listagem em Linha'), (2, 'Galeria Albuns'), (3, 'Página dos Parlamentares'), (4, 'Página individual de Parlamentar'), (5, 'Banco de Imagens'), (6, 'Galeria de Áudios'), (7, 'Galeria de Vídeos'), (99, 'Documento Específico')], default=1, verbose_name='Template para a Classe'),
        ),
    ]