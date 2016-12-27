# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0003_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='people',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
