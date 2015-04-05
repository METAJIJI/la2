# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20150402_2250'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='server',
            table='server_status',
        ),
    ]
