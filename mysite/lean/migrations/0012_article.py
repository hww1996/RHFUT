# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0011_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField(verbose_name='正文')),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
