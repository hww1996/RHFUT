# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0009_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
