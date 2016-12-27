# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0037_auto_20160118_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='zhouer',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='zhousan',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='zhousi',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='zhouwu',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='zhouyi',
            options={'ordering': ['-timestamp']},
        ),
    ]
