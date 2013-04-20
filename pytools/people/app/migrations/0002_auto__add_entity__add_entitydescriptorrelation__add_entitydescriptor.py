# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entity'
        db.create_table(u'app_entity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('graph_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'app', ['Entity'])

        # Adding model 'EntityDescriptorRelation'
        db.create_table(u'app_entitydescriptorrelation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Entity'])),
            ('relation', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('entity_descriptor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.EntityDescriptor'])),
            ('best_description', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['EntityDescriptorRelation'])

        # Adding model 'EntityDescriptor'
        db.create_table(u'app_entitydescriptor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'app', ['EntityDescriptor'])


    def backwards(self, orm):
        # Deleting model 'Entity'
        db.delete_table(u'app_entity')

        # Deleting model 'EntityDescriptorRelation'
        db.delete_table(u'app_entitydescriptorrelation')

        # Deleting model 'EntityDescriptor'
        db.delete_table(u'app_entitydescriptor')


    models = {
        u'app.entity': {
            'Meta': {'object_name': 'Entity'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'graph_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'app.entitydescriptor': {
            'Meta': {'object_name': 'EntityDescriptor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'app.entitydescriptorrelation': {
            'Meta': {'object_name': 'EntityDescriptorRelation'},
            'best_description': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Entity']"}),
            'entity_descriptor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.EntityDescriptor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relation': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'app.names': {
            'Meta': {'object_name': 'Names'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'crawled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'app.people': {
            'Meta': {'object_name': 'People'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['app']