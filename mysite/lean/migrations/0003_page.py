# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0002_auto_20151021_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('people', models.ForeignKey(to='lean.people')),
            ],
        ),
    ]
