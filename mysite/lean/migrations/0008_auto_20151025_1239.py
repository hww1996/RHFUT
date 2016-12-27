# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0007_remove_people_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='lean.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='people',
        ),
    ]
