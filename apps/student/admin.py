# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from apps.student.models import Student

# Register your models here.

admin.site.register(Student)