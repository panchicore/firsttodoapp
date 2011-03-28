# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Todo.descripcion'
        db.add_column('tada_todo', 'descripcion', self.gf('django.db.models.fields.CharField')(default='por default', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Todo.descripcion'
        db.delete_column('tada_todo', 'descripcion')


    models = {
        'tada.todo': {
            'Meta': {'object_name': 'Todo'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
