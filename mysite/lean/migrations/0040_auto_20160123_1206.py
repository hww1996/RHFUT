# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0039_auto_20160123_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='category',
            field=models.CharField(verbose_name='类别', max_length=4, choices=[('周一', '周一'), ('周二', '周二'), ('周三', '周三'), ('周四', '周四'), ('周五', '周五')]),
        ),
    ]
