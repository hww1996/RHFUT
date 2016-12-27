# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0053_auto_20160402_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uparticle',
            name='author',
            field=models.CharField(verbose_name='作者', max_length=100, default='匿名'),
        ),
    ]
