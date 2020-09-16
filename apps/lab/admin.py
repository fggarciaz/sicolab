# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from apps.lab.models import Lab, Computer

# Register your models here.

admin.site.register(Lab)
admin.site.register(Computer)