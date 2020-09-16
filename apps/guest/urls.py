from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.guest.views import GuestCreate, GuestUpdate, GuestDelete, GuestList, GuestAPI_List, GuestAPI_Detail, UsersDate

urlpatterns = [
    url(r'^invitado/nuevo/$', GuestCreate.as_view(), name='guest_crear'),
    url(r'^invitado/editar/(?P<pk>\d+)/$', GuestUpdate.as_view(), name='guest_editar'),
    url(r'^invitado/eliminar/(?P<pk>\d+)/$', GuestDelete.as_view(), name='guest_eliminar'),
    url(r'^invitado/listar/$', GuestList.as_view(), name='guest_listar'),
    url(r'^api/guest/$', login_required(GuestAPI_List)),
    url(r'^api/guest/(?P<pk>[0-9]+)/$', login_required(GuestAPI_Detail)),
    url(r'^invitado/exter/$', UsersDate, name='invitado_exter'),

    
 ]