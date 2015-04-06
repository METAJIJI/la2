from django.db import models
from django.contrib.auth.models import User


class ServerLogin(models.Model):
    user = models.ForeignKey(User)
    login = models.CharField(max_length=128)


User.login = property(lambda u: ServerLogin.objects.get_or_create(user=u)[0])

