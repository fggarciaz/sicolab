from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.administrator.views import AdministratorCreate, AdministratorUpdate, AdministratorDelete, AdministratorList

urlpatterns = [
    url(r'^administrador/nuevo/$', login_required(AdministratorCreate.as_view()), name='administrator_crear'),
    url(r'^administrador/editar/(?P<pk>\d+)/$', login_required(AdministratorUpdate.as_view()), name='administrator_editar'),
    url(r'^administrador/eliminar/(?P<pk>\d+)/$', login_required(AdministratorDelete.as_view()), name='administrator_eliminar'),
    url(r'^administrador/listar/$', login_required(AdministratorList.as_view()), name='administrator_listar'),
 ]