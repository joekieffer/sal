# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
import string
import random

class Migration(SchemaMigration):
    def GenerateKey():
        key = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(128))
        try:
            orm.MachineGroup.objects.get(key=key)
            return GenerateKey()
        except MachineGroup.DoesNotExist:
            return key;
    def forwards(self, orm):
        # Deleting field 'BusinessUnit.key'
        db.delete_column(u'server_businessunit', 'key')

        # Deleting field 'MachineGroup.manifest'
        db.delete_column(u'server_machinegroup', 'manifest')

        # Adding field 'MachineGroup.key'
        db.add_column(u'server_machinegroup', 'key',
                      self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True),
                      keep_default=False)
        
        for group in orm.MachineGroup.objects.all():
                group.key = GenerateKey()
                group.save()


    def backwards(self, orm):
        # Adding field 'BusinessUnit.key'
        db.add_column(u'server_businessunit', 'key',
                      self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MachineGroup.manifest'
        db.add_column(u'server_machinegroup', 'manifest',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=256),
                      keep_default=False)

        # Deleting field 'MachineGroup.key'
        db.delete_column(u'server_machinegroup', 'key')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'server.businessunit': {
            'Meta': {'ordering': "['name']", 'object_name': 'BusinessUnit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
        },
        u'server.fact': {
            'Meta': {'ordering': "['fact_name']", 'object_name': 'Fact'},
            'fact_data': ('django.db.models.fields.TextField', [], {}),
            'fact_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Machine']"})
        },
        u'server.machine': {
            'Meta': {'ordering': "['hostname']", 'object_name': 'Machine'},
            'activity': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'console_user': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'cpu_speed': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'cpu_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hd_percent': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'hd_space': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'hd_total': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'machine_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.MachineGroup']"}),
            'machine_model': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'memory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'memory_kb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'munki_version': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'report': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'warnings': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'server.machinegroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'MachineGroup'},
            'business_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.BusinessUnit']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'server.pendingappleupdate': {
            'Meta': {'ordering': "['display_name']", 'unique_together': "(('machine', 'update'),)", 'object_name': 'PendingAppleUpdate'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Machine']"}),
            'update': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'update_version': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'server.pendingupdate': {
            'Meta': {'ordering': "['display_name']", 'unique_together': "(('machine', 'update'),)", 'object_name': 'PendingUpdate'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Machine']"}),
            'update': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'update_version': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'server.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'SO'", 'max_length': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['server']