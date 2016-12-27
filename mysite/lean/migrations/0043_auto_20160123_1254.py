# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0042_auto_20160123_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='reporter1',
            field=models.CharField(verbose_name='主播1', max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='reporter2',
            field=models.CharField(verbose_name='主播2', max_length=50, default=''),
            preserve_default=False,
        ),
    ]
