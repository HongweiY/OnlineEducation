# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-25 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='idea',
            field=models.CharField(default='\u4e00\u5207\u4e3a\u4e86\u5b66\u751f', max_length=30, verbose_name='\u673a\u6784\u7406\u5ff5'),
        ),
    ]
