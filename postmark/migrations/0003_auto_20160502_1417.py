# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postmark', '0002_auto_20141028_2212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailbounce',
            options={'get_latest_by': 'bounced_at', 'verbose_name': 'email bounce', 'verbose_name_plural': 'email bounces'},
        ),
    ]