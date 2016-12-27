# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0031_auto_20151121_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
