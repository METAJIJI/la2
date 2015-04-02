# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('login', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=256)),
                ('lastactive', models.IntegerField(default='0')),
                ('access_level', models.IntegerField(default='0')),
                ('lastip', models.CharField(default='', max_length=15, db_column='lastIP', blank=True)),
                ('lastserver', models.IntegerField(default='1', null=True, db_column='lastServer', blank=True)),
                ('comments', models.TextField(blank=True)),
                ('email', models.CharField(max_length=45)),
                ('pay_stat', models.IntegerField(default='1')),
                ('bonus', models.FloatField(default='1')),
                ('bonus_expire', models.IntegerField(default='0')),
                ('banexpires', models.IntegerField(default='0', db_column='banExpires')),
                ('allowips', models.CharField(default='*', max_length=256, db_column='AllowIPs')),
                ('lock_expire', models.IntegerField(default=604800)),
                ('activated', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'accounts',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
