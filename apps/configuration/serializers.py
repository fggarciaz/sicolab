# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.configuration.models import Configuration

class ConfigurationSerializer(ModelSerializer):

	class Meta:
		model = Configuration
		fields = ('id', 'stage_config', 'lock_all', 'update_at')