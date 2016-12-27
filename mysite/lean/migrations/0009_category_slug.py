# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0008_auto_20151025_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, default=''),
            preserve_default=False,
        ),
    ]
