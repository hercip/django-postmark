# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-19 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postmark', '0006_remove_emailmessage_headers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailmessage',
            old_name='headers_hstore',
            new_name='headers',
        ),
    ]