# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
import datetime


# Create your models here.
class Administrator(models.Model):
	dni_adm = models.CharField(unique= True, max_length=10)
	names_adm=models.CharField(max_length=150)
	email_adm = models.EmailField(max_length=100)
	password_adm = models.CharField(max_length=200)
	token_reset = models.CharField(max_length=200)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField()

	def __str__ (self):
		return '{}'.format(self.names_adm)