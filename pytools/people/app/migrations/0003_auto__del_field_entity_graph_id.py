# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Entity.graph_id'
        db.delete_column(u'app_entity', 'graph_id')


    def backwards(self, orm):
        # Adding field 'Entity.graph_id'
        db.add_column(u'app_entity', 'graph_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)


    models = {
        u'app.entity': {
            'Meta': {'object_name': 'Entity'},
            'description': ('django.db.models.fields.TextField', [], {}),
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