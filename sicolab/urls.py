"""sicolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, \
    password_reset, password_reset_done,password_reset_confirm, password_reset_complete
# from django.conf.urls import handler404, handler500
# from apps.career.views import mi_error_404, mi_error_500
"""
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
"""

urlpatterns = [  
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^sicolab/logout/', logout_then_login, name='logout'),
    url(r'^sicolab/', include('apps.home.urls', namespace='home')),
    url(r'^sicolab/', include('apps.lab.urls', namespace='lab')),
    url(r'^sicolab/', include('apps.lab.urls', namespace='computer')),
    url(r'^sicolab/', include('apps.career.urls', namespace='career')),
    url(r'^sicolab/', include('apps.career.urls', namespace='semester')),
    url(r'^sicolab/', include('apps.teacher.urls', namespace='teacher')),
    url(r'^sicolab/', include('apps.teacher.urls', namespace='subject')),
    url(r'^sicolab/', include('apps.student.urls', namespace='student')),
    url(r'^sicolab/', include('apps.schedule.urls', namespace='schedule')),    
    url(r'^sicolab/', include('apps.administrator.urls', namespace='administrator')),
    url(r'^sicolab/', include('apps.configuration.urls', namespace='configuration')),
    url(r'^sicolab/', include('apps.notify.urls', namespace='notify')),
    url(r'^sicolab/', include('apps.guest.urls', namespace='guest')),
    url(r'^sicolab/', include('apps.session.urls',namespace='internal')),    
    url(r'^sicolab/', include('apps.session.urls',namespace='external')),
    url(r'^sicolab/', include('apps.distributive.urls',namespace='distributive')),
    url(r'^sicolab/', include('apps.distributive.urls',namespace='stage')),
    url(r'^sicolab/', include('apps.usuario.urls', namespace='usuario')), 
    url(r'^sicolab/', include('apps.auth.urls', namespace='api-auth')),

    url(r'^reset/password_reset$', password_reset, {'template_name':'restauracion_password/password_reset_form.html',
        'email_template_name':'restauracion_password/password_reset_email.html'}, name='password_reset'), 
    url(r'^reset/password_reset_done$',password_reset_done, {'template_name':'restauracion_password/password_reset_envio.html'},
         name='password_reset_done' ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,{'template_name':'restauracion_password/password_reset_confirm.html'},
         name='password_reset_confirm'),
    url(r'^reset/done$',password_reset_complete,{'template_name':'restauracion_password/password_reset_complete.html'}, name='password_reset_complete')
 
]

# handler404 = mi_error_404
# handler500 = mi_error_500