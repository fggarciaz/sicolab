# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.

class Career(models.Model):
	id_car = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	name_car = models.CharField(unique=True, max_length=100)
	section_car = models.CharField(max_length=100)

	def __str__ (self):
		return '{}'.format(self.name_car)

	def __getitem__(self, item):
		return getattr(self, item)

class Semester(models.Model):
	id_sem = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	name_sem = models.CharField(max_length=100)
	parallel_sem = models.CharField(max_length=1)
	#year_sem = models.SmallIntegerField()
	car = models.ForeignKey(Career, on_delete=models.PROTECT)

	def __str__ (self):
		return '{}'.format(self.name_sem) + " " +'{}'.format(self.parallel_sem) \
			+ " | " +'{}'.format(self.car)

	def get_full_information (self):
		return '%s %s | %s' %(self.name_sem, self.parallel_sem, self.car)

	def __getitem__(self, item):
		return getattr(self, item)