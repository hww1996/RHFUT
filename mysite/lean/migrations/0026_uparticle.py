# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0025_auto_20151120_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='题目', max_length=100)),
                ('author', models.CharField(verbose_name='作者', max_length=100)),
                ('content', models.TextField(verbose_name='内容', max_length=3000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
