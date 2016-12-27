# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0006_people_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='slug',
        ),
    ]
