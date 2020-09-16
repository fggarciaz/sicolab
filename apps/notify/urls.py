from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.notify.views import NotifyList, NotifyAPI_List, update_notify, NotifyAPI_Detail,NotifyAjax_List,NotifyDelete

urlpatterns = [
	url(r'^notificacion/listar/$', login_required(NotifyList.as_view()), name='notify_listar'),
	url(r'^notificacion/update/$', login_required(update_notify), name='notify_update'),
	url(r'^api/notify/$', NotifyAPI_List.as_view()),
	url(r'^api/notify_current/$', NotifyAjax_List),
    url(r'^api/notify/(?P<pk>[0-9]+)/$', NotifyAPI_Detail.as_view()), 
	url(r'^notificacionion/ver/(?P<pk>\d+)/$', login_required(NotifyDelete.as_view()), name='notify_eliminar'),

    
 ]