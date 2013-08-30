# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Projeto.responsavel'
        db.delete_column('projeto_projeto', 'responsavel_id')

        # Deleting field 'Projeto.area'
        db.delete_column('projeto_projeto', 'area_id')

        # Adding field 'Projeto.demandante'
        db.add_column('projeto_projeto', 'demandante',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='area_demandante_projeto', to=orm['projeto.Area']),
                      keep_default=False)

        # Adding field 'Projeto.demandada'
        db.add_column('projeto_projeto', 'demandada',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='area_demandada_projeto', to=orm['projeto.Area']),
                      keep_default=False)

        # Adding field 'Area.responsavel'
        db.add_column('projeto_area', 'responsavel',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='responsavel_area', to=orm['projeto.Pessoa']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Projeto.responsavel'
        db.add_column('projeto_projeto', 'responsavel',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['projeto.Pessoa']),
                      keep_default=False)

        # Adding field 'Projeto.area'
        db.add_column('projeto_projeto', 'area',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['projeto.Area']),
                      keep_default=False)

        # Deleting field 'Projeto.demandante'
        db.delete_column('projeto_projeto', 'demandante_id')

        # Deleting field 'Projeto.demandada'
        db.delete_column('projeto_projeto', 'demandada_id')

        # Deleting field 'Area.responsavel'
        db.delete_column('projeto_area', 'responsavel_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projeto.acompanhamentoiteracao': {
            'Meta': {'ordering': "['-ativo', 'iteracao__nome', 'mc__user__username', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'AcompanhamentoIteracao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Iteracao']"}),
            'mc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Pessoa']"}),
            'objetivo': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'real': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'realizado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.andamento': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Andamento'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Item']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Status']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.area': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Area'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Area']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'responsavel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'responsavel_area'", 'to': "orm['projeto.Pessoa']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.artefato': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Artefato'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.configuracao': {
            'Meta': {'object_name': 'Configuracao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'chave': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'projeto.equipe': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Equipe'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pessoas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projeto.Pessoa']", 'through': "orm['projeto.EquipePessoa']", 'symmetrical': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.equipepessoa': {
            'Meta': {'object_name': 'EquipePessoa'},
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'equipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Equipe']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Pessoa']"})
        },
        'projeto.fato': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Fato'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 1, 11, 0, 0)'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Iteracao']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ocorrencias': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'1'"}),
            'pessoas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projeto.Pessoa']", 'through': "orm['projeto.FatoPessoa']", 'symmetrical': 'False'}),
            'tempo': ('django.db.models.fields.CharField', [], {'default': "'1:00:00'", 'max_length': '10'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Tipo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.fatopessoa': {
            'Meta': {'object_name': 'FatoPessoa'},
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fato': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Fato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Pessoa']"})
        },
        'projeto.item': {
            'Meta': {'object_name': 'Item'},
            'andamentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projeto.Status']", 'through': "orm['projeto.Andamento']", 'symmetrical': 'False'}),
            'artefato': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Artefato']"}),
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'demandada': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandada_item'", 'to': "orm['projeto.Area']"}),
            'demandante': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandante_item'", 'to': "orm['projeto.Area']"}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Iteracao']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'responsavel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Pessoa']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Tipo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.iteracao': {
            'Meta': {'object_name': 'Iteracao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_fim': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 1, 23, 0, 0)'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 1, 11, 0, 0)'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_dias_nao_uteis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pessoas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projeto.Pessoa']", 'through': "orm['projeto.IteracaoPessoa']", 'symmetrical': 'False'}),
            'predecessora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Iteracao']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Projeto']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.iteracaopessoa': {
            'Meta': {'object_name': 'IteracaoPessoa'},
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Iteracao']"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Pessoa']"})
        },
        'projeto.pessoa': {
            'Meta': {'ordering': "['-user__is_active', 'user__username', 'user__first_name', 'user__last_name', 'user__email', 'observacoes', '-data_hora_atualizacao', '-user__date_joined']", 'object_name': 'Pessoa'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_pessoa'", 'to': "orm['projeto.Area']"}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.projeto': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Projeto'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'demandada': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandada_projeto'", 'to': "orm['projeto.Area']"}),
            'demandante': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandante_projeto'", 'to': "orm['projeto.Area']"}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.status': {
            'Meta': {'object_name': 'Status'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'predecessora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Status']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'projeto.tipo': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Tipo'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['projeto']
