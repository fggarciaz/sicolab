# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from apps.teacher.models import Subject
from apps.distributive.models import Distributive
from apps.lab.models import Lab

# Create your models here.


import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.


class Schedule(models.Model):
	#stage = models.CharField(max_length=6)
	id_sched = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	day = models.CharField(max_length=1)
	hour_start = models.TimeField(auto_now=False, auto_now_add=False)
	hour_end = models.TimeField(auto_now=False, auto_now_add=False)
	#year_sem = models.SmallIntegerField()
	lab = models.ForeignKey(Lab, related_name='sched', on_delete=models.PROTECT)
	#sub = models.ForeignKey(Subject, on_delete=models.PROTECT)
	dist = models.ForeignKey(Distributive, related_name='schedules', on_delete=models.PROTECT)
	
	def __str__ (self):
		return '{}'.format(self.day) + " | " +'{}'.format(self.hour_start) + " " +'{}'.format(self.hour_end) \
			+ " | " +'{}'.format(self.lab) + " " +'{}'.format(self.dist)
	
	def get_full_information (self):
		return '%s %s %s %s %s' %(self.day, self.hour_start, self.hour_end,  self.lab, self.dist)
