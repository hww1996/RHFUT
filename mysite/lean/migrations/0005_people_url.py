# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0004_auto_20151024_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='url',
            field=models.URLField(default='www.baidu.com'),
            preserve_default=False,
        ),
    ]
