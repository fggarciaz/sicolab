# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from apps.lab.models import Computer

import datetime

# Create your models here.
class Notify(models.Model):
	message = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)
	finish_session = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField()
	type_notify = models.SmallIntegerField()
	comp = models.ForeignKey(Computer, on_delete=models.PROTECT)
	ci = models.CharField(max_length=10)

	def __str__(self):
		return '{}'.format(self.message)