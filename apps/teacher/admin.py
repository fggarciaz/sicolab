# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from apps.teacher.models import Teacher, Subject

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Subject)