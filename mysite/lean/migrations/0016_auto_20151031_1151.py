# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0015_auto_20151031_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content_new',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
