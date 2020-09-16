from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.usuario.views import UsuarioCreate, UsuarioList, UsuarioUpdate, UsuarioDelete

urlpatterns = [
    #url(r'^user/$', index, name='index'),
    url(r'^admin/registrar/$', login_required(UsuarioCreate.as_view()), name='registrar'),    
    url(r'^admin/listar/$', login_required(UsuarioList.as_view()), name='listar'),
    url(r'^admin/actualizar/(?P<pk>\d+)/$', login_required(UsuarioUpdate.as_view()), name='actualizar'),
    url(r'^admin/eliminar/(?P<pk>\d+)/$', login_required(UsuarioDelete.as_view()), name='eliminar'),
    #url(r'^editar/(?P<pk>\d+)/$', LabUpdate.as_view(), name='lab_editar'),
    #url(r'^eliminar/(?P<pk>\d+)/$', LabDelete.as_view(), name='lab_eliminar'),
    #url(r'^$', LabList.as_view(), name='lab_listar'),
]