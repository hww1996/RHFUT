# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0049_auto_20160401_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporters',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='reporters',
            name='summary',
            field=models.CharField(default='', verbose_name='简介', max_length=100),
            preserve_default=False,
        ),
    ]
