# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0021_auto_20151031_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('music_name', models.CharField(verbose_name='歌名', max_length=100)),
                ('music_singer', models.CharField(verbose_name='歌手', max_length=100)),
                ('music_number', models.CharField(choices=[('一首', '一首'), ('两首', '两首'), ('三首', '三首'), ('四首', '四首'), ('NO', 'NO')], max_length=2)),
                ('message', models.TextField(verbose_name='留言', max_length=140)),
            ],
        ),
    ]
