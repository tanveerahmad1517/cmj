# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0002_auto_20160801_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='pronometratamento',
            name='prefixo_nome_plural_f',
            field=models.CharField(default='', max_length=254, verbose_name='Prefixo Plural Feminino'),
        ),
        migrations.AddField(
            model_name='pronometratamento',
            name='prefixo_nome_plural_m',
            field=models.CharField(default='', max_length=254, verbose_name='Prefixo Plural Masculino'),
        ),
        migrations.AddField(
            model_name='pronometratamento',
            name='prefixo_nome_singular_f',
            field=models.CharField(default='', max_length=254, verbose_name='Prefixo Singular Feminino'),
        ),
        migrations.AddField(
            model_name='pronometratamento',
            name='prefixo_nome_singular_m',
            field=models.CharField(default='', max_length=254, verbose_name='Prefixo Singular Masculino'),
        ),
    ]
