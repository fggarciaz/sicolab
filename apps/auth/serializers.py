# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.student.models import Student

class LoginSerializer(ModelSerializer):

	class Meta:
		model = Student
		fields = ('dni_stu', 'password_stu')