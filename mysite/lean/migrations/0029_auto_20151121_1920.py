# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0028_auto_20151121_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='biaobai',
            name='name',
            field=models.CharField(db_column='表白', default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='huodong',
            name='name',
            field=models.CharField(db_column='活动', default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shiwu',
            name='name',
            field=models.CharField(db_column='失物', default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tucao',
            name='name',
            field=models.CharField(db_column='吐槽', default='', max_length=10),
            preserve_default=False,
        ),
    ]
