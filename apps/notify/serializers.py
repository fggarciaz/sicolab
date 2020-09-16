# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.notify.models import Notify

class NotifySerializer(ModelSerializer):

	class Meta:
		model = Notify
		fields = ('id', 'message', 'create_at', 'finish_session', 'status', 'type_notify', 'comp','ci')