# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0024_auto_20151120_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biaobai',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='huodong',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shiwu',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tucao',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
