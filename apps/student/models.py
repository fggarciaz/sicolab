# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import md5
from django.db import models
import datetime
#from apps.teacher.models import Subject
from apps.distributive.models import Distributive

# Create your models here.

class Student(models.Model):
	id_stu = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	dni_stu = models.CharField(unique=True, max_length=10)
	password_stu = models.CharField(max_length=200)
	names_stu = models.CharField(max_length=150)
	email_stu = models.EmailField(unique=True, max_length=100)
	token_reset = models.CharField(max_length=200)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	status_stu = models.SmallIntegerField()
	dist = models.ManyToManyField(Distributive, blank=True)

	def save(self, *args, **kwargs):
		if(self.password_stu=="" or self.password_stu==self.dni_stu):
			self.password_stu = md5.new(self.dni_stu).hexdigest()
		super(Student, self).save(*args, **kwargs)

	def __str__ (self):
		return '{}'.format(self.names_stu)

	def __getitem__(self, item):
		return getattr(self, item)