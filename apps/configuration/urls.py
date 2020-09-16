from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.configuration.views import ConfigurationUpdate, ConfigurationList, ConfigurationAPI_List, ConfigurationAPI_Detail

urlpatterns = [
   # url(r'^configuration/editar/$', login_required(ConfigurationUpdate.as_view()), name='configuration_editar'),
    url(r'^configuracion/editar/(?P<pk>\d+)/$', login_required(ConfigurationUpdate.as_view()), name='configuration_editar'),
    url(r'^configuracion/listar/$', login_required(ConfigurationList.as_view()), name='configuration_listar'),
    url(r'^api/configuration/$', login_required(ConfigurationAPI_List)),
    url(r'^api/configuration/(?P<pk>[0-9]+)/$', login_required(ConfigurationAPI_Detail)),
 ]