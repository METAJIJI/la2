from django.db import models
import socket


class State(models.Model):
    active = models.BooleanField(default=True)
    server = models.CharField(max_length=20, default='server')




