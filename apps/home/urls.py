from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from apps.home.views import index
from django.contrib.auth.decorators import login_required
from apps.home.views import LabList

urlpatterns = [
    url(r'^index/$', login_required(LabList.as_view()), name='index'),
]