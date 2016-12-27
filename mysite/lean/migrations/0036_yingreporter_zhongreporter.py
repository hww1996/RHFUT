# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0035_auto_20151128_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yingreporter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', unique=True, max_length=100)),
                ('content', ckeditor.fields.RichTextField(verbose_name='简介')),
            ],
        ),
        migrations.CreateModel(
            name='Zhongreporter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=100)),
                ('content', ckeditor.fields.RichTextField(verbose_name='简介')),
            ],
        ),
    ]
