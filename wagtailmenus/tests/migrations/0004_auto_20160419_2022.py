# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20160418_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='subnav_menu_text',
            new_name='repeated_item_text',
        ),
        migrations.RenameField(
            model_name='toplevelpage',
            old_name='subnav_menu_text',
            new_name='repeated_item_text',
        ),
    ]