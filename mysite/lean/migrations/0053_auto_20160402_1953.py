# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0052_auto_20160401_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='category',
            field=models.CharField(verbose_name='类别', choices=[('周一', '周一'), ('周二', '周二'), ('周三', '周三'), ('周四', '周四'), ('周五', '周五'), ('早间节目', '早间节目')], max_length=4),
        ),
        migrations.AlterField(
            model_name='qiang',
            name='author',
            field=models.CharField(verbose_name='作者', default='匿名', max_length=20),
        ),
    ]
