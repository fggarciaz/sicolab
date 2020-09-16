# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.session.models import Internal, External

class InternalSerializer(ModelSerializer):

	class Meta:
		model = Internal
		#hola = 'hola'		
		fields = ('id_inter', 'start_time', 'finish_time', 'finish_session', 'status', 'type_user', 'id_user', 'comp')

class ExternalSerializer(ModelSerializer):

	class Meta:
		model = External
		fields = ('id_exter', 'name_user', 'start_time', 'finish_time', 'finish_session', 'status', 'guest', 'comp')