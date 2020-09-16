# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from apps.lab.models import Computer
from apps.guest.models import Guest

# Create your models here.

class Internal(models. Model):
	id_inter = models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	finish_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	finish_session = models.DateTimeField(auto_now=False, auto_now_add=False)
	status = models.SmallIntegerField()
	type_user = models.CharField(max_length=1)
	id_user = models.BigIntegerField()
	comp = models.ForeignKey(Computer, on_delete=models.PROTECT)

	def __getitem__(self, item):
		return getattr(self, item)

class External(models. Model):
	id_exter = models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
	name_user = models.CharField(max_length=200)
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	finish_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	finish_session = models.DateTimeField(auto_now=False, auto_now_add=False)
	status = models.SmallIntegerField()	
	guest = models.ForeignKey(Guest, on_delete=models.PROTECT)
	comp = models.ForeignKey(Computer, on_delete=models.PROTECT)

	def __str__ (self):
		return '{}'.format(self.name_user)

	def __getitem__(self, item):
		return getattr(self, item)