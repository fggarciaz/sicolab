# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from apps.lab.models import Lab
import datetime

# Create your models here.

class Guest(models.Model):
	id_guest = models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
	description = models.CharField(unique=True, max_length=200)
	password_access = models.CharField(max_length=200)
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	finish_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField()
	lab = models.ForeignKey(Lab, on_delete=models.PROTECT)

	def __str__ (self):
		return '{}'.format(self.description) #+ " " +'{}'.format(self.start_time) + " " +'{}'.format(self.finish_time) \
			#+ " " +'{}'.format(self.status) #+ " | " +'{}'.format(self.id_lab)

	def get_full_information (self):
		return '%s %s %s %s' %(self.description, self.start_time, self.finish_time, self.status)