# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.guest.models import Guest

class GuestSerializer(ModelSerializer):

	class Meta:
		model = Guest
		fields = ('id_guest', 'description', 'password_access', 'start_time', 'finish_time', 'created_at', 'updated_at', 'status', 'lab')