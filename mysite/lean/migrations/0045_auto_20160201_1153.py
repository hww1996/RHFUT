# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0044_reporters_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporters',
            name='category',
            field=models.CharField(max_length=4, choices=[('中文主播', '中文主播'), ('英文主播', '英文主播')], verbose_name='类别'),
        ),
    ]
