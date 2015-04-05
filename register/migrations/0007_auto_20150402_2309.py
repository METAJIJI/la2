# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20150402_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'managed': False},
        ),
    ]
