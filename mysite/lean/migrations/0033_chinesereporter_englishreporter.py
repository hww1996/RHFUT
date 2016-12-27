# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0032_music_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chinesereporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='姓名', max_length=100, unique=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='简介')),
            ],
        ),
        migrations.CreateModel(
            name='Englishreporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='姓名', max_length=100, unique=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='简介')),
            ],
        ),
    ]
