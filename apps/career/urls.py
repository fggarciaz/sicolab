from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.career.views import CareerCreate, CareerUpdate, CareerDelete, CareerList, CareerReport, \
	SemesterCreate, SemesterUpdate, SemesterDelete, SemesterList, SemesterAPI_List, SemesterAPI_Detail, SemesterReport

urlpatterns = [
    url(r'^carrera/nuevo/$', login_required(CareerCreate.as_view()), name='career_crear'),
    url(r'^carrera/editar/(?P<pk>\d+)/$', login_required(CareerUpdate.as_view()), name='career_editar'),
    url(r'^carrera/eliminar/(?P<pk>\d+)/$', login_required(CareerDelete.as_view()), name='career_eliminar'),
    url(r'^carrera/listar/$', login_required(CareerList.as_view()), name='career_listar'),
    url(r'^carrera/reporte/$', login_required(CareerReport), name='career_reporte'),    

    url(r'^semestre/nuevo/$', login_required(SemesterCreate.as_view()), name='semester_crear'),
    url(r'^semestre/editar/(?P<pk>\d+)/$', login_required(SemesterUpdate.as_view()), name='semester_editar'),
    url(r'^semestre/eliminar/(?P<pk>\d+)/$', login_required(SemesterDelete.as_view()), name='semester_eliminar'),
    url(r'^semestre/listar/$', login_required(SemesterList.as_view()), name='semester_listar'),
    url(r'^semestre/reporte/$', login_required(SemesterReport), name='semester_reporte'),    
    url(r'^api/semester/$', login_required(SemesterAPI_List)),
    url(r'^api/semester/(?P<pk>[0-9]+)/$', login_required(SemesterAPI_Detail)),
    
]