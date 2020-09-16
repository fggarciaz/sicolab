# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer, StringRelatedField
from apps.distributive.models import Stage, Distributive
from apps.schedule.serializers import ScheduleSerializer


class StageSerializer(ModelSerializer):

	class Meta:
		model = Stage
		fields = ('id_sta', 'name_sta', 'start_date', 'end_date')

class DistributiveSerializer(ModelSerializer):
	#schedules = StringRelatedField(many=True)
	schedules = ScheduleSerializer(many=True)

	class Meta:
		model = Distributive
		fields = ('id_dist', 'sta', 'sem', 'tea', 'sub', 'schedules')

class DistributiveSerializerApi(ModelSerializer):
	#schedules = StringRelatedField(many=True)
	#schedules = ScheduleSerializer(many=True)

	class Meta:
		model = Distributive
		fields = ('id_dist', 'sta', 'sem', 'tea', 'sub')