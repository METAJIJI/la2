
from __future__ import unicode_literals
from django.db import models
import whirlpool
import base64

class Accounts(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=128,
                                help_text=("Use '[algo]$[salt]$[hexdigest]' "
                                           "or use the <a href=\"password/\">change password form</a>."))
    lastactive = models.IntegerField(default='0')
    access_level = models.IntegerField(default='0')
    lastip = models.CharField(db_column='lastIP', max_length=15, blank=True, default='')  # Field name made lowercase.
    lastserver = models.IntegerField(db_column='lastServer', blank=True, null=True,
                                     default='1')  # Field name made lowercase.
    comments = models.TextField(blank=True)
    email = models.CharField(max_length=45)
    pay_stat = models.IntegerField(default='1')
    bonus = models.FloatField(default='1')
    bonus_expire = models.IntegerField(default='0')
    banexpires = models.IntegerField(db_column='banExpires', default='0')  # Field name made lowercase.
    allowips = models.CharField(db_column='AllowIPs', max_length=256, default='*')  # Field name made lowercase.
    lock_expire = models.IntegerField(default=604800)
    activated = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'accounts'

    def set_passwords(self, raw_password):
        wp = whirlpool.new(raw_password)
        self.password = base64.b64encode(wp.digest())

    def check_password(self, password):
        pass
