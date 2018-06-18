# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_evento_solicitante'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ('-inicio',), 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AddField(
            model_name='evento',
            name='link_externo',
            field=models.URLField(blank=True, default='', verbose_name='Url Externa'),
        ),
    ]