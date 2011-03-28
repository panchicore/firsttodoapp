# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Todo'
        db.create_table('tada_todo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('tada', ['Todo'])

        # Adding model 'TodoItem'
        db.create_table('tada_todoitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('todo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['tada.Todo'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=233)),
            ('hecha', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tada', ['TodoItem'])


    def backwards(self, orm):
        
        # Deleting model 'Todo'
        db.delete_table('tada_todo')

        # Deleting model 'TodoItem'
        db.delete_table('tada_todoitem')


    models = {
        'tada.todo': {
            'Meta': {'object_name': 'Todo'},
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
