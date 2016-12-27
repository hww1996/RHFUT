# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0056_play'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('category', models.CharField(max_length=32, verbose_name='类别')),
                ('reporter', models.ManyToManyField(to='lean.Reporters')),
            ],
        ),
        migrations.RemoveField(
            model_name='program',
            name='category',
        ),
        migrations.AddField(
            model_name='program',
            name='category',
            field=models.ManyToManyField(to='lean.Programcategory'),
        ),
    ]
