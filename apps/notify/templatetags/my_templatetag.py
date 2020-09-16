# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from apps.notify.models import Notify
from apps.lab.models import Lab,Computer
from apps.student.models import Student
from apps.teacher.models import Teacher

from django import template

register = template.Library()

@register.simple_tag
def get_listNotify():
	return Notify.objects.all()

@register.simple_tag
def get_countNotify():	
	return Notify.objects.filter(status=1).count()

@register.simple_tag
def get_Computer():	
	return Computer.objects.all()

@register.simple_tag
def get_Studen():	
	return Student.objects.all()

@register.simple_tag
def get_Profe():	
	return Teacher.objects.all()