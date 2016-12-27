# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0043_auto_20160123_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporters',
            name='partner',
            field=models.CharField(default='', max_length=100, verbose_name='搭档', unique=True),
            preserve_default=False,
        ),
    ]
