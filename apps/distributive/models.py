# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from apps.teacher.models import Teacher, Subject
from apps.career.models import Semester

# Create your models here.

class Stage(models.Model):
	id_sta = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	name_sta = models.CharField(unique=True, max_length=6)
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__ (self):
		return '{}'.format(self.name_sta)

class Distributive(models.Model):
	id_dist = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')		
	sta = models.ForeignKey(Stage, on_delete=models.PROTECT)
	sem = models.ForeignKey(Semester, on_delete=models.PROTECT)
	tea = models.ForeignKey(Teacher, related_name='dist', on_delete=models.PROTECT)
	sub = models.ForeignKey(Subject, on_delete=models.PROTECT)

	def __str__ (self):
		return '{}'.format(self.sta) + \
		" " + '{}'.format(self.sem) + \
		" | " + '{}'.format(self.tea) + \
		" | " + '{}'.format(self.sub)

	def get_information (self):
		return '%' %(self.sub)

	def __getitem__(self, item):
		return getattr(self, item)