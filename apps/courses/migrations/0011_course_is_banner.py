# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-27 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20170923_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u63a8\u8350\u8bfe\u7a0b'),
        ),
    ]
