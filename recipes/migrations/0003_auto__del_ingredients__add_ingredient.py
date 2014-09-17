# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Ingredients'
        db.delete_table('recipes_ingredients')

        # Adding model 'Ingredient'
        db.create_table('recipes_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Food'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('measurement', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('recipes', ['Ingredient'])


    def backwards(self, orm):
        # Adding model 'Ingredients'
        db.create_table('recipes_ingredients', (
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Food'])),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('measurement', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('recipes', ['Ingredients'])

        # Deleting model 'Ingredient'
        db.delete_table('recipes_ingredient')


    models = {
        'recipes.food': {
            'Meta': {'object_name': 'Food'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Food']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement': ('django.db.models.fields.SmallIntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '80'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['recipes']