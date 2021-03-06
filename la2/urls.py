from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from register.views import *
from check.views import *
from statistics.views import *
from cabinet.views import *


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^news', RedirectView.as_view(url='/')),
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', register),
    url(r'^complete/', complete),
    url(r'^show/', show),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^cabinet/$', cabinet),
    url(r'^cabinet/(?P<server>(\w+))/$', cabinet),
    url(r'^cabinet/(?P<server>(\w+))/(?P<login>(\w+))/$', show_account),
    url(r'^cabinet/(?P<server>(\w+))/(?P<login>(\w+))/(?P<login_id>(\w+))/(?P<sort>(\w+))/(?P<order>(\w+))/$', show_character),

    url(r'^change/(?P<login>[^\.]+)$', change_password),
    url(r'^changed/', changed),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^statistics/players/$', players),
    url(r'^statistics/players/(\d{1,2})/$', players),
    url(r'^statistics/players/(\d{1,2}?)/(\d{1,2}?)/$', players),

    url(r'^statistics/castles/$', castles),
    url(r'^statistics/castles/(?P<server>(\w+))/$', castles),

    url(r'^statistics/clans/$', clans),
    url(r'^statistics/clans/(?P<server>(\w+))/$', clans),
    url(r'^statistics/clans/(?P<server>(\w+))/(?P<clanid>(\w+))/$', clan_members),

    )