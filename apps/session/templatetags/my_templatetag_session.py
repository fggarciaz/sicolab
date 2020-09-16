# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from apps.student.models import Student
from apps.teacher.models import Teacher

from django import template

register = template.Library()

@register.simple_tag
def get_Student():
	return Student.objects.all()

@register.simple_tag
def get_Teacher():
	return Teacher.objects.all()