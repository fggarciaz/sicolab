from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.distributive.views import DistributiveCreate, DistributiveUpdate, DistributiveDelete, DistributiveList, DistributiveAPI_List, DistributiveAPI_Detail, DistributiveReport,\
	StageCreate, StageUpdate, StageDelete, StageList, StageAPI_List, StageAPI_Detail

urlpatterns = [
    url(r'^distributivo/nuevo/$', login_required(DistributiveCreate.as_view()), name='distributive_crear'),
    url(r'^distributivo/editar/(?P<pk>\d+)/$', login_required(DistributiveUpdate.as_view()), name='distributive_editar'),
    url(r'^distributivo/eliminar/(?P<pk>\d+)/$', login_required(DistributiveDelete.as_view()), name='distributive_eliminar'),
    url(r'^distributivo/listar/$', login_required(DistributiveList.as_view()), name='distributive_listar'),
    url(r'^distributivo/reporte/$', login_required(DistributiveReport), name='distributive_reporte'),
    url(r'^api/distributive/$', login_required(DistributiveAPI_List.as_view())),
    url(r'^api/distributive/(?P<pk>[0-9]+)/$', login_required(DistributiveAPI_Detail.as_view())),

    url(r'^periodo/nuevo/$', login_required(StageCreate.as_view()), name='stage_crear'),
    url(r'^periodo/editar/(?P<pk>\d+)/$', login_required(StageUpdate.as_view()), name='stage_editar'),
    url(r'^periodo/eliminar/(?P<pk>\d+)/$', login_required(StageDelete.as_view()), name='stage_eliminar'),
    url(r'^periodo/listar/$', login_required(StageList.as_view()), name='stage_listar'),
    url(r'^api/stage/$', login_required(StageAPI_List.as_view())),
    url(r'^api/stage/(?P<pk>[0-9]+)/$', login_required(StageAPI_Detail.as_view())),
 ]