# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0018_auto_20151031_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
