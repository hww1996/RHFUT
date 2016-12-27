# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0020_auto_20151031_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='biaoti',
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Biaoti',
        ),
    ]
