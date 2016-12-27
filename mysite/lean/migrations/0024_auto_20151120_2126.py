# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0023_auto_20151120_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='biaobai',
            name='time',
            field=models.DateTimeField(verbose_name='时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='huodong',
            name='time',
            field=models.DateTimeField(verbose_name='时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shiwu',
            name='time',
            field=models.DateTimeField(verbose_name='时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tucao',
            name='time',
            field=models.DateTimeField(verbose_name='时间'),
            preserve_default=False,
        ),
    ]
