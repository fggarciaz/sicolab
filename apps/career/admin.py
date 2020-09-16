# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from apps.career.models import Career, Semester

# Register your models here.

admin.site.register(Career)
admin.site.register(Semester)