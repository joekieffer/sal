# Generated by Django 2.1.4 on 2019-03-05 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0091_remove_machine_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='errors',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='warnings',
        ),
    ]
