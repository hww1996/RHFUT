# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0036_yingreporter_zhongreporter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qiang',
            options={'ordering': ['-time']},
        ),
    ]
