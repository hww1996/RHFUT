# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0005_people_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='slug',
            field=models.SlugField(default='lean', unique=True),
            preserve_default=False,
        ),
    ]
