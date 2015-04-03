# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_auto_20150403_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='server',
            field=models.CharField(default=b'server', max_length=10),
            preserve_default=True,
        ),
    ]
