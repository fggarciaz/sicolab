# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
import datetime
import md5

from apps.career.models import Semester

# Create your models here.

class Teacher(models.Model):
	id_tea = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	dni_tea = models.CharField(unique=True, max_length=10)
	password_tea = models.CharField(max_length=200)
	names_tea = models.CharField(unique=True, max_length=150)
	email_tea = models.EmailField(unique=True, max_length=100)
	token_reset = models.CharField(max_length=200)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField()

	# def save(self, *args, **kwargs):
	# 	if(self.password_tea==""):
	# 		self.password_tea = md5.new(self.dni_tea).hexdigest()
	# 	super(Teacher, self).save(*args, **kwargs)

	def __str__ (self):
		return '{}'.format(self.names_tea)

	def __getitem__(self, item):
		return getattr(self, item)


class Subject(models.Model):
	id_sub = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')	
	name_sub = models.CharField(unique=True, max_length=150)
	#stage_sub = models.CharField(max_length=6)
	#sem = models.ForeignKey(Semester, on_delete=models.PROTECT)
	#tea = models.ForeignKey(Teacher, on_delete=models.PROTECT)

	def __str__(self):
		return '{}'.format(self.name_sub)

	def __getitem__(self, item):
		return getattr(self, item)