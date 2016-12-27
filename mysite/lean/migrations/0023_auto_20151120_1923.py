# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0022_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biaobai',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='题目')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('content', models.TextField(max_length=140, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Huodong',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='题目')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('content', models.TextField(max_length=140, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Shiwu',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='题目')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('content', models.TextField(max_length=140, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Tucao',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='题目')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('content', models.TextField(max_length=140, verbose_name='内容')),
            ],
        ),
        migrations.AlterField(
            model_name='music',
            name='music_number',
            field=models.CharField(max_length=2, choices=[('一首', '一首'), ('两首', '两首'), ('三首', '三首'), ('四首', '四首'), ('NO', 'NO')], verbose_name='歌曲数量'),
        ),
    ]
