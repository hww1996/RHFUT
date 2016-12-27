# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0033_chinesereporter_englishreporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zhouer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, verbose_name='题目', max_length=100)),
                ('author', models.CharField(verbose_name='作者', max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name='时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Zhousan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, verbose_name='题目', max_length=100)),
                ('author', models.CharField(verbose_name='作者', max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name='时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Zhousi',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, verbose_name='题目', max_length=100)),
                ('author', models.CharField(verbose_name='作者', max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name='时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Zhouwu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, verbose_name='题目', max_length=100)),
                ('author', models.CharField(verbose_name='作者', max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name='时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Zhouyi',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, verbose_name='题目', max_length=100)),
                ('author', models.CharField(verbose_name='作者', max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name='时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
        ),
    ]
