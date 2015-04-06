from django.contrib import admin
from extend_user.models import ServerLogin

class Extend(admin.ModelAdmin):
    list_display = ['user', 'login']


admin.site.register(ServerLogin, Extend)