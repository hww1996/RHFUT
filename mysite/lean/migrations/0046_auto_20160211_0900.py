# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0045_auto_20160201_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='reporter1',
        ),
        migrations.RemoveField(
            model_name='program',
            name='reporter2',
        ),
        migrations.AddField(
            model_name='program',
            name='summary',
            field=models.CharField(default='', verbose_name='简介', max_length=256),
            preserve_default=False,
        ),
    ]
