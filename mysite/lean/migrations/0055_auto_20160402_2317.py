# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0054_auto_20160402_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoupdata',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 15, 17, 0, 529370, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photoupdata',
            name='usage',
            field=models.CharField(max_length=30, verbose_name='用于（周几的文章）', default='周一'),
        ),
    ]
