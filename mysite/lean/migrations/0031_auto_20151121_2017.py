# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0030_auto_20151121_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qiang',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='类别', choices=[('吐槽', '吐槽'), ('表白', '表白'), ('失物', '失物'), ('活动', '活动')], max_length=2)),
                ('title', models.CharField(verbose_name='题目', max_length=50)),
                ('author', models.CharField(verbose_name='作者', max_length=20)),
                ('content', models.TextField(verbose_name='内容', max_length=140)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Biaobai',
        ),
        migrations.DeleteModel(
            name='Huodong',
        ),
        migrations.DeleteModel(
            name='Shiwu',
        ),
        migrations.DeleteModel(
            name='Tucao',
        ),
    ]
