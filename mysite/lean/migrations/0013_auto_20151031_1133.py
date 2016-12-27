# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0012_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='content_new',
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AddField(
            model_name='content',
            name='article',
            field=models.ForeignKey(to='lean.Article'),
        ),
    ]
