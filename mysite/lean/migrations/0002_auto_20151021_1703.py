# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='age',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
