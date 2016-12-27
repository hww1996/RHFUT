# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0047_auto_20160401_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='use',
            name='headImg',
            field=models.FileField(upload_to='./lean/static/zhubo/'),
        ),
    ]
