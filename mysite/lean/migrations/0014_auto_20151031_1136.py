# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0013_auto_20151031_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='article',
        ),
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
