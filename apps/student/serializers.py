# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer
from apps.student.models import Student
from apps.distributive.serializers import DistributiveSerializer

import md5

class StudentSerializer(ModelSerializer):
	dist = DistributiveSerializer(many=True, read_only=True)

	class Meta:
		model = Student
		fields = ('id_stu', 'dni_stu', 'password_stu', 'names_stu', 'email_stu', 'token_reset', 'status_stu', 'dist')

class StudentSerializer2(ModelSerializer):
	class Meta:
		model = Student
		fields = ('id_stu', 'password_stu')
		#read_only_fields = ('password_stu',)

	def update(self, instance, validated_data):
		#instance = self.get_object()
		instance.password_stu = md5.new(validated_data.get('password_stu', instance.password_stu)).hexdigest()
		instance.save()
		return instance