# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Todo.descripcion'
        db.alter_column('tada_todo', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Todo.nombre'
        db.alter_column('tada_todo', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=512))


    def backwards(self, orm):
        
        # Changing field 'Todo.descripcion'
        db.alter_column('tada_todo', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Todo.nombre'
        db.alter_column('tada_todo', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
        'tada.todo': {
            'Meta': {'object_name': 'Todo'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'tada.todoitem': {
            'Meta': {'object_name': 'TodoItem'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '233'}),
            'hecha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'todo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['tada.Todo']"})
        }
    }

    complete_apps = ['tada']
