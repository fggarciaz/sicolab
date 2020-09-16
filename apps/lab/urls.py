from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.lab.views import index, LabCreate, LabUpdate, LabDelete, LabList, LabAPI_List, LabAPI_Detail, LabReport, \
	ComputerCreate, ComputerUpdate, ComputerDelete, ComputerList, ComputerAPI_List, ComputerAPI_Detail, ComputerAPI_Detail2, ComputerReport

urlpatterns = [
    url(r'^lab/$', index, name='index'),
    url(r'^laboratorio/nuevo/$', login_required(LabCreate.as_view()), name='lab_crear'),
    url(r'^laboratorio/editar/(?P<pk>\d+)/$', login_required(LabUpdate.as_view()), name='lab_editar'),
    url(r'^laboratorio/eliminar/(?P<pk>\d+)/$', login_required(LabDelete.as_view()), name='lab_eliminar'),
    url(r'^laboratorio/listar/$', login_required(LabList.as_view()), name='lab_listar'),
    url(r'^laboratorio/reporte/$', login_required(LabReport), name='lab_reporte'),
    url(r'^api/lab/$', LabAPI_List.as_view()),
    url(r'^api/lab/(?P<pk>[0-9]+)/$', LabAPI_Detail.as_view()),

    url(r'^computador/nuevo/$', login_required(ComputerCreate.as_view()), name='computer_crear'),
    url(r'^computador/editar/(?P<pk>\d+)/$', login_required(ComputerUpdate.as_view()), name='computer_editar'),
    url(r'^computador/eliminar/(?P<pk>\d+)/$', login_required(ComputerDelete.as_view()), name='computer_eliminar'),
    url(r'^computador/listar/$', login_required(ComputerList.as_view()), name='computer_listar'),
    url(r'^computador/reporte/$', login_required(ComputerReport), name='computer_reporte'),
    url(r'^api/computer/$', ComputerAPI_List.as_view()),
    #url(r'^api/computer/(?P<pk>[0-9]+)/$', ComputerAPI_Detail.as_view()),
    url(r'^api/computer/verify/(?P<mac_comp>.+)/$', ComputerAPI_Detail.as_view()),
    url(r'^api/computer/(?P<mac_comp>.+)/$', ComputerAPI_Detail2.as_view()),
]