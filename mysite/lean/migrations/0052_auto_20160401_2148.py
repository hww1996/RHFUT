# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lean', '0051_auto_20160401_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='photoupdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(default='请输入相片的名字', verbose_name='相片名字', max_length=30)),
                ('headImg', models.FileField(upload_to='./lean/static/program/')),
            ],
        ),
        migrations.DeleteModel(
            name='use',
        ),
        migrations.AlterField(
            model_name='reporters',
            name='summary',
            field=models.CharField(max_length=1000, verbose_name='主播总结'),
        ),
    ]
