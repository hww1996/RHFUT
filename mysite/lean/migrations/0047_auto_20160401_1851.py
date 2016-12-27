# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0046_auto_20160211_0900'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='use',
        ),
    ]
