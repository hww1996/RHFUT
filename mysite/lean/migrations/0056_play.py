# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0055_auto_20160402_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='play',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('number1', models.IntegerField()),
                ('number2', models.IntegerField()),
            ],
        ),
    ]
