# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import md5
from rest_framework.serializers import ModelSerializer
from apps.teacher.models import Teacher, Subject
from apps.distributive.serializers import DistributiveSerializer

class TeacherSerializer(ModelSerializer):
	dist = DistributiveSerializer(many=True)

	class Meta:
		model = Teacher
		fields = ('id_tea', 'dni_tea', 'password_tea', 'names_tea', 'email_tea', 'token_reset', 'status', 'dist')
			

class SubjectSerializer(ModelSerializer):

	class Meta:
		model = Subject
		fields = ('id_sub', 'name_sub')

class TeacherSerializer2(ModelSerializer):
	class Meta:
		model = Teacher
		fields = ('id_tea', 'password_tea')
		#read_only_fields = ('password_stu',)

	def update(self, instance, validated_data):
		#instance = self.get_object()
		instance.password_tea = md5.new(validated_data.get('password_tea', instance.password_tea)).hexdigest()
		instance.save()
		return instance