# -*- coding: utf-8 -*-
from django.db import models
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Status'
        db.create_table(u'projeto_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('predecessora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Status'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'projeto', ['Status'])

        # Adding model 'Artefato'
        db.create_table(u'projeto_artefato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'projeto', ['Artefato'])

        # Adding model 'Tipo'
        db.create_table(u'projeto_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'projeto', ['Tipo'])

        # Adding model 'Area'
        db.create_table(u'projeto_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Area'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'projeto', ['Area'])

        # Adding model 'Pessoa'
        db.create_table(u'projeto_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'projeto', ['Pessoa'])

        # Adding model 'AreaPessoa'
        db.create_table(u'projeto_areapessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Area'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Pessoa'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Tipo'])),
        ))
        db.send_create_signal(u'projeto', ['AreaPessoa'])

        # Adding model 'Configuracao'
        db.create_table(u'projeto_configuracao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('chave', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'projeto', ['Configuracao'])

        # Adding model 'Projeto'
        db.create_table(u'projeto_projeto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('responsavel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Pessoa'])),
            ('demandante', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_demandante_projeto', to=orm['projeto.Area'])),
            ('demandada', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_demandada_projeto', to=orm['projeto.Area'])),
        ))
        db.send_create_signal(u'projeto', ['Projeto'])

        # Adding model 'Iteracao'
        db.create_table(u'projeto_iteracao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('data_inicio', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 6, 0, 0))),
            ('data_fim', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 18, 0, 0))),
            ('numero_dias_nao_uteis', self.gf('django.db.models.fields.PositiveIntegerField')(default=5)),
            ('predecessora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Iteracao'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('projeto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Projeto'])),
        ))
        db.send_create_signal(u'projeto', ['Iteracao'])

        # Adding model 'IteracaoPessoa'
        db.create_table(u'projeto_iteracaopessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_hora_inicio', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_fim', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('iteracao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Iteracao'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Pessoa'])),
        ))
        db.send_create_signal(u'projeto', ['IteracaoPessoa'])

        # Adding model 'AcompanhamentoIteracao'
        db.create_table(u'projeto_acompanhamentoiteracao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('objetivo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('real', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('realizado', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('mc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Pessoa'])),
            ('iteracao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Iteracao'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'projeto', ['AcompanhamentoIteracao'])

        # Adding model 'Equipe'
        db.create_table(u'projeto_equipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'projeto', ['Equipe'])

        # Adding model 'EquipePessoa'
        db.create_table(u'projeto_equipepessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_hora_inicio', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_fim', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('equipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Equipe'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Pessoa'])),
        ))
        db.send_create_signal(u'projeto', ['EquipePessoa'])

        # Adding model 'Fato'
        db.create_table(u'projeto_fato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('data', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 6, 0, 0))),
            ('ocorrencias', self.gf('django.db.models.fields.PositiveIntegerField')(default='1')),
            ('tempo', self.gf('django.db.models.fields.CharField')(default='1:00:00', max_length=10)),
            ('iteracao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Iteracao'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Tipo'])),
        ))
        db.send_create_signal(u'projeto', ['Fato'])

        # Adding model 'FatoPessoa'
        db.create_table(u'projeto_fatopessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_hora_inicio', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_fim', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('fato', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Fato'])),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Pessoa'])),
        ))
        db.send_create_signal(u'projeto', ['FatoPessoa'])

        # Adding model 'Item'
        db.create_table(u'projeto_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Item'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('artefato', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Artefato'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Tipo'])),
            ('responsavel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Pessoa'])),
            ('demandante', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_demandante_item', to=orm['projeto.Area'])),
            ('demandada', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_demandada_item', to=orm['projeto.Area'])),
            ('iteracao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Iteracao'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'projeto', ['Item'])

        # Adding model 'Andamento'
        db.create_table(u'projeto_andamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('excluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_hora_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('data_hora_inicio', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_hora_fim', self.gf('django.db.models.fields.DateTimeField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Item'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Status'])),
        ))
        db.send_create_signal(u'projeto', ['Andamento'])


    def backwards(self, orm):
        # Deleting model 'Status'
        db.delete_table(u'projeto_status')

        # Deleting model 'Artefato'
        db.delete_table(u'projeto_artefato')

        # Deleting model 'Tipo'
        db.delete_table(u'projeto_tipo')

        # Deleting model 'Area'
        db.delete_table(u'projeto_area')

        # Deleting model 'Pessoa'
        db.delete_table(u'projeto_pessoa')

        # Deleting model 'AreaPessoa'
        db.delete_table(u'projeto_areapessoa')

        # Deleting model 'Configuracao'
        db.delete_table(u'projeto_configuracao')

        # Deleting model 'Projeto'
        db.delete_table(u'projeto_projeto')

        # Deleting model 'Iteracao'
        db.delete_table(u'projeto_iteracao')

        # Deleting model 'IteracaoPessoa'
        db.delete_table(u'projeto_iteracaopessoa')

        # Deleting model 'AcompanhamentoIteracao'
        db.delete_table(u'projeto_acompanhamentoiteracao')

        # Deleting model 'Equipe'
        db.delete_table(u'projeto_equipe')

        # Deleting model 'EquipePessoa'
        db.delete_table(u'projeto_equipepessoa')

        # Deleting model 'Fato'
        db.delete_table(u'projeto_fato')

        # Deleting model 'FatoPessoa'
        db.delete_table(u'projeto_fatopessoa')

        # Deleting model 'Item'
        db.delete_table(u'projeto_item')

        # Deleting model 'Andamento'
        db.delete_table(u'projeto_andamento')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projeto.acompanhamentoiteracao': {
            'Meta': {'ordering': "['-ativo', 'iteracao__nome', 'mc__user__username', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'AcompanhamentoIteracao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Iteracao']"}),
            'mc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Pessoa']"}),
            'objetivo': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'real': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'realizado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.andamento': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Andamento'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Item']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Status']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.area': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Area'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Area']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.areapessoa': {
            'Meta': {'object_name': 'AreaPessoa'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Area']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Pessoa']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Tipo']"})
        },
        u'projeto.artefato': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Artefato'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.configuracao': {
            'Meta': {'object_name': 'Configuracao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'chave': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'projeto.equipe': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Equipe'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pessoas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projeto.Pessoa']", 'through': u"orm['projeto.EquipePessoa']", 'symmetrical': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.equipepessoa': {
            'Meta': {'object_name': 'EquipePessoa'},
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'equipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Equipe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Pessoa']"})
        },
        u'projeto.fato': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Fato'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 6, 0, 0)'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Iteracao']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ocorrencias': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'1'"}),
            'pessoas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projeto.Pessoa']", 'through': u"orm['projeto.FatoPessoa']", 'symmetrical': 'False'}),
            'tempo': ('django.db.models.fields.CharField', [], {'default': "'1:00:00'", 'max_length': '10'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Tipo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.fatopessoa': {
            'Meta': {'object_name': 'FatoPessoa'},
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fato': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Fato']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Pessoa']"})
        },
        u'projeto.item': {
            'Meta': {'object_name': 'Item'},
            'andamentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projeto.Status']", 'through': u"orm['projeto.Andamento']", 'symmetrical': 'False'}),
            'artefato': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Artefato']"}),
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'demandada': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandada_item'", 'to': u"orm['projeto.Area']"}),
            'demandante': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandante_item'", 'to': u"orm['projeto.Area']"}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Iteracao']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Item']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'responsavel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Pessoa']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Tipo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.iteracao': {
            'Meta': {'object_name': 'Iteracao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_fim': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 18, 0, 0)'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 6, 0, 0)'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numero_dias_nao_uteis': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pessoas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projeto.Pessoa']", 'through': u"orm['projeto.IteracaoPessoa']", 'symmetrical': 'False'}),
            'predecessora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Iteracao']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Projeto']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.iteracaopessoa': {
            'Meta': {'object_name': 'IteracaoPessoa'},
            'data_hora_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_hora_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iteracao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Iteracao']"}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Pessoa']"})
        },
        u'projeto.pessoa': {
            'Meta': {'ordering': "['-user__is_active', 'user__username', 'user__first_name', 'user__last_name', 'user__email', 'observacoes', '-data_hora_atualizacao', '-user__date_joined']", 'object_name': 'Pessoa'},
            'area': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projeto.Area']", 'through': u"orm['projeto.AreaPessoa']", 'symmetrical': 'False'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.projeto': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Projeto'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'demandada': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandada_projeto'", 'to': u"orm['projeto.Area']"}),
            'demandante': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_demandante_projeto'", 'to': u"orm['projeto.Area']"}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'responsavel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Pessoa']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.status': {
            'Meta': {'object_name': 'Status'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'predecessora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projeto.Status']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'projeto.tipo': {
            'Meta': {'ordering': "['-ativo', 'nome', 'observacoes', '-data_hora_atualizacao', '-data_hora_criacao']", 'object_name': 'Tipo'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'data_hora_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_hora_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observacoes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['projeto']