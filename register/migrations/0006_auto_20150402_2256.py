# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20150402_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='id',
        ),
        migrations.AlterField(
            model_name='server',
            name='active',
            field=models.IntegerField(default='0', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='server',
            table=None,
        ),
    ]
