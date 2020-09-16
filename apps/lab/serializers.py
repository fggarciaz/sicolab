# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.lab.models import Lab, Computer
from apps.schedule.models import Schedule
from apps.schedule.serializers import ScheduleSerializer
from apps.schedule.views import ScheduleAPI_List

class LabSerializer(ModelSerializer):
	#data = Schedule.objects.filter(day=2)
	sched = ScheduleSerializer(many=True)
	#sched = ScheduleAPI_List(many=True)

	class Meta:
		model = Lab
		fields = ('id_lab', 'name_lab', 'sched')

class ComputerSerializer(ModelSerializer):

	class Meta:
		model = Computer
		fields = ('id_comp', 'name_comp', 'mac_comp', 'ip_comp', 'lab')
