# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0041_auto_20160123_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='reporter1',
        ),
        migrations.RemoveField(
            model_name='program',
            name='reporter2',
        ),
    ]
