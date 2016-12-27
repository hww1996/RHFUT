# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0034_zhouer_zhousan_zhousi_zhouwu_zhouyi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chinesereporter',
        ),
        migrations.DeleteModel(
            name='Englishreporter',
        ),
    ]
