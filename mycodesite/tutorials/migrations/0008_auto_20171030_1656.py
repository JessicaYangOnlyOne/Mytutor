# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-30 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_auto_20171029_1643'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='session',
            name='tutorials_s_tutor_u_097bb7_idx',
        ),
    ]
