# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('nome', models.CharField(blank=True, default='', max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Área de Trabalho',
                'verbose_name_plural': 'Áreas de Trabalho',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_social', models.CharField(blank=True, default='', max_length=100, verbose_name='Nome Social')),
                ('apelido', models.CharField(blank=True, default='', max_length=100, verbose_name='Apelido')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(blank=True, choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, verbose_name='Sexo Biológico')),
                ('identidade_genero', models.CharField(blank=True, default='', max_length=100, verbose_name='Como se reconhece?')),
                ('tem_filhos', models.NullBooleanField(choices=[(None, '---------'), (True, 'Sim'), (False, 'Não')], default=None, verbose_name='Tem Filhos?')),
                ('quantos_filhos', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Quantos Filhos?')),
                ('naturalidade', models.CharField(blank=True, max_length=50, verbose_name='Naturalidade')),
                ('nome_pai', models.CharField(blank=True, max_length=100, verbose_name='Nome do Pai')),
                ('nome_mae', models.CharField(blank=True, max_length=100, verbose_name='Nome da Mãe')),
                ('numero_sus', models.CharField(blank=True, max_length=100, verbose_name='Número do SUS')),
                ('cpf', models.CharField(blank=True, max_length=15, verbose_name='CPF')),
                ('titulo_eleitor', models.CharField(blank=True, max_length=15, verbose_name='Título de Eleitor')),
                ('rg', models.CharField(blank=True, max_length=30, verbose_name='RG')),
                ('rg_orgao_expedidor', models.CharField(blank=True, max_length=20, verbose_name='Órgão Expedidor')),
                ('rg_data_expedicao', models.DateField(blank=True, null=True, verbose_name='Data de Expedição')),
                ('ativo', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Ativo?')),
                ('profissao', models.CharField(blank=True, max_length=254, verbose_name='Profissão')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_social', models.CharField(blank=True, default='', max_length=100, verbose_name='Nome Social')),
                ('apelido', models.CharField(blank=True, default='', max_length=100, verbose_name='Apelido')),
                ('sexo', models.CharField(blank=True, choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data Nascimento')),
                ('identidade_genero', models.CharField(blank=True, default='', max_length=100, verbose_name='Como você se reconhece?')),
            ],
            options={
                'verbose_name': 'Dependente',
                'verbose_name_plural': 'Dependentes',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('preferencial', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Preferêncial?')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': "Email's",
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PA', 'Pará'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins'), ('EX', 'Exterior')], max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(blank=True, default='', max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(blank=True, default='', help_text='O campo endereço também é um campo de busca, nele você pode digitar qualquer informação, inclusive digitar o cep para localizar o endereço, e vice-versa!', max_length=254, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, default='', max_length=50, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, default='', max_length=254, verbose_name='Bairro')),
                ('complemento', models.CharField(blank=True, default='', max_length=30, verbose_name='Complemento')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'verbose_name_plural': 'Estados Civis',
            },
        ),
        migrations.CreateModel(
            name='FiliacaoPartidaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data de Filiação')),
                ('data_desfiliacao', models.DateField(blank=True, null=True, verbose_name='Data de Desfiliação')),
            ],
            options={
                'verbose_name': 'Filiação Partidária',
                'verbose_name_plural': 'Filiações Partidárias',
            },
        ),
        migrations.CreateModel(
            name='LocalTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome / Razão Social')),
                ('nome_social', models.CharField(blank=True, default='', max_length=254, verbose_name='Nome Fantasia')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PA', 'Pará'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins'), ('EX', 'Exterior')], max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(blank=True, default='', max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(blank=True, default='', help_text='O campo endereço também é um campo de busca, nele você pode digitar qualquer informação, inclusive digitar o cep para localizar o endereço, e vice-versa!', max_length=254, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, default='', max_length=50, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, default='', max_length=254, verbose_name='Bairro')),
                ('complemento', models.CharField(blank=True, default='', max_length=30, verbose_name='Complemento')),
                ('data_inicio', models.DateField(blank=True, null=True, verbose_name='Data de Início')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Data de Fim')),
            ],
            options={
                'verbose_name': 'Local de Trabalho',
                'verbose_name_plural': 'Locais de Trabalho',
            },
        ),
        migrations.CreateModel(
            name='NivelInstrucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Nível de Instrução',
                'verbose_name_plural': 'Níveis de Instrução',
            },
        ),
        migrations.CreateModel(
            name='OperadorAreaTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('area_trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operadores_areatrabalho_set', to='cerimonial.AreaTrabalho', verbose_name='Área de Trabalho')),
                ('grupos_associados', models.ManyToManyField(related_name='operadores_areatrabalho_set', to='auth.Group', verbose_name='Grupos Associados')),
            ],
            options={
                'verbose_name': 'Operador',
                'verbose_name_plural': 'Operadores',
            },
        ),
        migrations.CreateModel(
            name='OperadoraTelefonia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Operadora de Telefonia',
                'verbose_name_plural': 'Operadoras de Telefonia',
            },
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Parentesco',
                'verbose_name_plural': 'Parentescos',
            },
        ),
        migrations.CreateModel(
            name='PronomeTratamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, default='', max_length=254, verbose_name='Nome / Descrição')),
                ('nome', models.CharField(default='', max_length=254, verbose_name='Nome')),
                ('abreviatura', models.CharField(default='', max_length=254, verbose_name='Abreviatura')),
            ],
            options={
                'verbose_name': 'Pronome de Tratamento',
                'verbose_name_plural': 'Pronomes de tratamento',
            },
        ),
        migrations.CreateModel(
            name='StatusVisita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Status da Visita',
                'verbose_name_plural': 'Status das Visitas',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('ddd', models.CharField(max_length=3, verbose_name='DDD')),
                ('numero', models.CharField(max_length=20, verbose_name='Número')),
                ('proprio', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Próprio?')),
                ('de_quem_e', models.CharField(blank=True, help_text='Se não é próprio, de quem é?', max_length=40, verbose_name='De quem é?')),
                ('preferencial', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Preferêncial?')),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cerimonial.Contato', verbose_name='Contato')),
                ('operadora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telefones_set', to='cerimonial.OperadoraTelefonia', verbose_name='Operadora de Telefonia')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='TipoAutoridade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
                ('pronome_tratamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tipo_autoridade_set', to='cerimonial.PronomeTratamento', verbose_name='Pronome de Tratamento')),
            ],
            options={
                'verbose_name': 'Tipo de Autoridade',
                'verbose_name_plural': 'Tipos de Autoridade',
            },
        ),
        migrations.CreateModel(
            name='TipoEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Email',
                'verbose_name_plural': 'Tipos de Email',
            },
        ),
        migrations.CreateModel(
            name='TipoEndereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Endereço',
                'verbose_name_plural': 'Tipos de Endereço',
            },
        ),
        migrations.CreateModel(
            name='TipoLocalTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Tipo do Local de Trabalho',
                'verbose_name_plural': 'Tipos de Local de Trabalho',
            },
        ),
        migrations.CreateModel(
            name='TipoTelefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Nome / Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Telefone',
                'verbose_name_plural': 'Tipos de Telefone',
            },
        ),
        migrations.AddField(
            model_name='telefone',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cerimonial.TipoTelefone', verbose_name='Tipo'),
        ),
    ]
