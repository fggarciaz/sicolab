# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from apps.notify.models import Notify

from django import template

register = template.Library()

@register.simple_tag
def get_listNotify():
	return Notify.objects.all()

@register.simple_tag
def get_countNotify():	
	return Notify.objects.filter(status=1).count()