# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0038_auto_20160118_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('category', models.CharField(verbose_name='类别', max_length=4, choices=[('中文主播', '中文主播'), ('英文主播', '英文文主播')])),
                ('title', models.CharField(unique=True, verbose_name='题目', max_length=100)),
                ('author', models.CharField(verbose_name='作者', max_length=50)),
                ('reporter_1', models.CharField(verbose_name='主播1', max_length=50)),
                ('reporter_2', models.CharField(verbose_name='主播2', max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name='时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Reporters',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('category', models.CharField(verbose_name='类别', max_length=4, choices=[('中文主播', '中文主播'), ('英文主播', '英文文主播')])),
                ('name', models.CharField(unique=True, verbose_name='姓名', max_length=100)),
                ('content', ckeditor.fields.RichTextField(verbose_name='简介')),
            ],
        ),
        migrations.DeleteModel(
            name='Yingreporter',
        ),
        migrations.DeleteModel(
            name='Zhongreporter',
        ),
        migrations.DeleteModel(
            name='Zhouer',
        ),
        migrations.DeleteModel(
            name='Zhousan',
        ),
        migrations.DeleteModel(
            name='Zhousi',
        ),
        migrations.DeleteModel(
            name='Zhouwu',
        ),
        migrations.DeleteModel(
            name='Zhouyi',
        ),
        migrations.AddField(
            model_name='program',
            name='reporter',
            field=models.ManyToManyField(to='lean.Reporters'),
        ),
    ]
