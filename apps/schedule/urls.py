from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.schedule.views import ScheduleCreate, ScheduleUpdate, ScheduleDelete, ScheduleList, ScheduleAPI_List, ScheduleAPI_Detail, ScheduleReport, \
	ScheduleImport, scheduleCargarExcel, scheduleCargarBase

urlpatterns = [
    url(r'^horario/nuevo/$', login_required(ScheduleCreate.as_view()), name='schedule_crear'),
    url(r'^horario/editar/(?P<pk>\d+)/$', login_required(ScheduleUpdate.as_view()), name='schedule_editar'),
    url(r'^horario/eliminar/(?P<pk>\d+)/$', login_required(ScheduleDelete.as_view()), name='schedule_eliminar'),
    url(r'^horario/listar/$', login_required(ScheduleList.as_view()), name='schedule_listar'),
    url(r'^horario/reporte/$', login_required(ScheduleReport), name='schedule_reporte'),
    url(r'^api/schedule/$', login_required(ScheduleAPI_List.as_view())),
    url(r'^api/schedule/(?P<pk>[0-9]+)/$', login_required(ScheduleAPI_Detail.as_view())),

	url(r'^horario/importar/$', login_required(ScheduleImport.as_view()), name='schedule_import'),
    url(r'^horario/subir/$', login_required(scheduleCargarExcel), name='schedule_cargarExcel'),
    url(r'^horario/db/$', login_required(scheduleCargarBase), name='schedule_cargarBase'),

]