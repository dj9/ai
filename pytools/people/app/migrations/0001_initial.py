# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'People'
        db.create_table(u'app_people', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'app', ['People'])

        # Adding model 'Names'
        db.create_table(u'app_names', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('crawled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('success', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['Names'])


    def backwards(self, orm):
        # Deleting model 'People'
        db.delete_table(u'app_people')

        # Deleting model 'Names'
        db.delete_table(u'app_names')


    models = {
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