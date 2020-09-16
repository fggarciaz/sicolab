from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.teacher.views import TeacherCreate, TeacherUpdate, TeacherDelete, TeacherList, TeacherAPI_List, TeacherAPI_Detail, TeacherReport, \
	SubjectCreate, SubjectUpdate, SubjectDelete, SubjectList, SubjectAPI_List, SubjectAPI_Detail, SubjectReport, \
    TeacherImport, teacherCargarExcel, teacherCargarBase, SubjectImport, subjectCargarExcel, subjectCargarBase

urlpatterns = [
    url(r'^docente/nuevo/$', login_required(TeacherCreate.as_view()), name='teacher_crear'),
    url(r'^docente/editar/(?P<pk>\d+)/$', login_required(TeacherUpdate.as_view()), name='teacher_editar'),
    url(r'^docente/eliminar/(?P<pk>\d+)/$', login_required(TeacherDelete.as_view()), name='teacher_eliminar'),
    url(r'^docente/listar/$', login_required(TeacherList.as_view()), name='teacher_listar'),
    url(r'^docente/reporte/$', login_required(TeacherReport), name='teacher_reporte'),

    url(r'^docente/importar/$', login_required(TeacherImport.as_view()), name='teacher_import'),
    url(r'^docente/subir/$', login_required(teacherCargarExcel), name='teacher_cargarExcel'),
    url(r'^docente/db/$', login_required(teacherCargarBase), name='teacher_cargarBase'),

    url(r'^api/teacher/$', login_required(TeacherAPI_List.as_view())),
    url(r'^api/teacher/(?P<pk>[0-9]+)/$', TeacherAPI_Detail.as_view()),
    #url(r'^api/teacher/(?P<dni_tea>[\w\-]+)/$', login_required(TeacherAPI_Detail.as_view())),    
    
    url(r'^asignatura/nuevo/$', login_required(SubjectCreate.as_view()), name='subject_crear'),
    url(r'^asignatura/editar/(?P<pk>\d+)/$', login_required(SubjectUpdate.as_view()), name='subject_editar'),
    url(r'^asignatura/eliminar/(?P<pk>\d+)/$', login_required(SubjectDelete.as_view()), name='subject_eliminar'),
    url(r'^asignatura/listar/$', login_required(SubjectList.as_view()), name='subject_listar'),
    url(r'^asignatura/reporte/$', login_required(SubjectReport), name='subject_reporte'),
    url(r'^api/subject/$', login_required(SubjectAPI_List.as_view())),
    url(r'^api/subject/(?P<pk>[0-9]+)/$', login_required(SubjectAPI_Detail.as_view())),

    url(r'^asignatura/importar/$', login_required(SubjectImport.as_view()), name='subject_import'),
    url(r'^asignatura/subir/$', login_required(subjectCargarExcel), name='subject_cargarExcel'),
    url(r'^asignatura/db/$', login_required(subjectCargarBase), name='subject_cargarBase'),

 ]