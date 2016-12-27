# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0026_uparticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='biaobai',
            name='name',
            field=models.CharField(null=True, max_length=10, db_column='表白'),
        ),
        migrations.AddField(
            model_name='huodong',
            name='name',
            field=models.CharField(null=True, max_length=10, db_column='活动'),
        ),
        migrations.AddField(
            model_name='shiwu',
            name='name',
            field=models.CharField(null=True, max_length=10, db_column='失物'),
        ),
        migrations.AddField(
            model_name='tucao',
            name='name',
            field=models.CharField(null=True, max_length=10, db_column='吐槽'),
        ),
    ]
