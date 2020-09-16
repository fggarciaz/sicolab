# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.student.views import StudentCreate, StudentUpdate, StudentDelete, StudentList, StudentReport,\
								StudentAPI_List, StudentAPI_Detail, Subject_StudentUpdate, Subject_StudentList, \
								StudentImport, studentCargarExcel, studentCargarBase

urlpatterns = [
	url(r'^estudiante/nuevo/$', login_required(StudentCreate.as_view()), name='student_crear'),
	url(r'^estudiante/editar/(?P<pk>\d+)/$', login_required(StudentUpdate.as_view()), name='student_editar'),
	url(r'^estudiante/eliminar/(?P<pk>\d+)/$', login_required(StudentDelete.as_view()), name='student_eliminar'),
	url(r'^estudiante/listar/$', login_required(StudentList.as_view()), name='student_listar'),
	url(r'^api/student/$', StudentAPI_List.as_view()),
	url(r'^api/student/(?P<pk>[0-9]+)/$', StudentAPI_Detail.as_view()),
	#url(r'^api/student/(?P<dni_stu>[\w\-]+)/$', StudentAPI_Detail.as_view()),
	url(r'^estudiante/reporte/$', login_required(StudentReport), name='student_reporte'),

	url(r'^estudiante/asignatura/(?P<pk>\d+)/$', login_required(Subject_StudentUpdate.as_view()), name='subject_student_editar'),
	url(r'^estudiante/asignatura/listar/$', login_required(Subject_StudentList.as_view()), name='subject_student_listar'),
	
	url(r'^estudiante/importar/$', login_required(StudentImport.as_view()), name='student_import'),
	url(r'^estudiante/subir/$', login_required(studentCargarExcel), name='student_cargarExcel'),
	url(r'^estudiante/db/$', login_required(studentCargarBase), name='student_cargarBase'),
 ]