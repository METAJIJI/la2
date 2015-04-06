# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extend_user', '0003_auto_20150406_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logins',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'logins',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='server',
            name='user',
        ),
        migrations.DeleteModel(
            name='Server',
        ),
    ]
