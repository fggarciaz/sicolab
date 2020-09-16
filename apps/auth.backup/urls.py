from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken import views as rest_framework_views
from apps.auth.views import studentLogin, externalLogin, getDistributive

urlpatterns = [
    url(r'^api-auth/get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^api/internal-login/$', studentLogin),
    url(r'^api/external-login/$', externalLogin),
    url(r'^api/get-distributive/$', getDistributive),
    #url(r'^api-auth/create/$', login_required(create_auth_token)),
    
]