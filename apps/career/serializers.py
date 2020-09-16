# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.career.models import Semester

class SemesterSerializer(ModelSerializer):

	class Meta:
		model = Semester
		fields = ('id_sem', 'name_sem', 'parallel_sem')