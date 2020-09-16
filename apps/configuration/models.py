# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
import datetime


# Create your models here.
class Configuration(models.Model):
	
	stage_config = models.CharField(max_length=6)
	lock_all = models.SmallIntegerField()
	update_at = models.DateTimeField(auto_now=True)
	
	# def __str__ (self):
	# 	return '{}'.format(self.names_adm)