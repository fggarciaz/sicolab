# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.

class Lab(models.Model):
	id_lab = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	name_lab = models.CharField(unique=True, max_length=100)
	#ip1_lab = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	#ip2_lab = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)

	def __str__(self):
		return '{}'.format(self.name_lab)

	def __getitem__(self, item):
		return getattr(self, item)

class Computer(models.Model):
	id_comp = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	name_comp = models.CharField(max_length=100)
	mac_comp = models.CharField(unique=True, max_length=20)
	ip_comp = models.CharField(max_length=20)
	lab = models.ForeignKey(Lab, on_delete=models.PROTECT)

	def __getitem__(self, item):
		return getattr(self, item)