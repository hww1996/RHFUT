# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0040_auto_20160123_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='reporter_1',
            new_name='reporter1',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='reporter_2',
            new_name='reporter2',
        ),
    ]
