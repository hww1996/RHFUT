# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0017_auto_20151031_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baioti',
            name='slug',
            field=models.SlugField(),
        ),
    ]
