# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0027_auto_20151121_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biaobai',
            name='name',
        ),
        migrations.RemoveField(
            model_name='huodong',
            name='name',
        ),
        migrations.RemoveField(
            model_name='shiwu',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tucao',
            name='name',
        ),
    ]
