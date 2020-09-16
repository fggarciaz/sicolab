from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.session.views import InternalList, ExternalList, InternalAPI_List, InternalAPI_Detail, \
	ExternalAPI_List, ExternalAPI_Detail, InternalReport, ExternalReport

urlpatterns = [
    url(r'^sesion/interna/listar/$', InternalList.as_view(), name='internal_listar'),
    url(r'^sesion/externa/listar/$', ExternalList.as_view(), name='external_listar'),
    url(r'^sesion/interna/reporte/$', login_required(InternalReport), name='internal_reporte'),
    url(r'^sesion/externa/reporte/$', login_required(ExternalReport), name='external_reporte'),
    url(r'^api/session/internal/$', InternalAPI_List.as_view()),
    url(r'^api/session/internal/(?P<pk>[0-9]+)/$', InternalAPI_Detail.as_view()),
    url(r'^api/session/external/$', ExternalAPI_List.as_view()),
    url(r'^api/session/external/(?P<pk>[0-9]+)/$', ExternalAPI_Detail.as_view()),
    
 ]