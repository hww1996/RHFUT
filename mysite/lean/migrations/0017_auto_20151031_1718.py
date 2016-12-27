# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0016_auto_20151031_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baioti',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='biaoti',
            field=models.ForeignKey(to='lean.Baioti', default=''),
            preserve_default=False,
        ),
    ]
