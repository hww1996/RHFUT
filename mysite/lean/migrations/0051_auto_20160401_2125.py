# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0050_auto_20160401_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporters',
            name='summary',
            field=models.CharField(verbose_name='简介', max_length=1000),
        ),
    ]
