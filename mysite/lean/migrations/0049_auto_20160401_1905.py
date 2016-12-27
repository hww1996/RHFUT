# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0048_auto_20160401_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporters',
            name='headImg',
            field=models.FileField(upload_to='./lean/static/zhubo/', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporters',
            name='timestamp',
            field=models.DateTimeField(default='2015-12-12 12:12', verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='music',
            name='message',
            field=models.TextField(verbose_name='留言', max_length=280),
        ),
        migrations.AlterField(
            model_name='qiang',
            name='content',
            field=models.TextField(verbose_name='内容', max_length=280),
        ),
        migrations.AlterField(
            model_name='uparticle',
            name='content',
            field=models.TextField(verbose_name='内容', max_length=6000),
        ),
    ]
