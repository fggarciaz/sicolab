# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

#import time
from rest_framework.serializers import ModelSerializer
from apps.schedule.models import Schedule

# hora_actual = time.strftime("%H:%M:%S")	
# dia_actual = time.strftime("%w")

class ScheduleSerializer(ModelSerializer):

	class Meta:
		model = Schedule
		#queryset = Schedule.objects.filter(day=dia_actual, hour_start__lte=hora_actual, hour_end__gte=hora_actual)
		fields = ('id_sched', 'day', 'hour_start', 'hour_end', 'lab', 'dist')