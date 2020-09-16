# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import time
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from apps.lab.models import Lab, Computer
from apps.schedule.models import Schedule
from apps.distributive.models import Distributive
from apps.teacher.models import Teacher, Subject
from apps.session.models import Internal
from django.views.generic import ListView, DetailView

# Create your views here.
#------ Vistas para Home

def index(request):
	#return HttpResponse("Hola")
	return render(request, 'index.html')

class LabList(ListView):

	queryset = Lab.objects.order_by('id_lab')
	template_name = 'index.html'	
	
	def get_context_data(self, **kwargs):
		hora_actual = time.strftime("%H:%M:%S")	
		dia_actual = time.strftime("%w")		
		context = super(LabList, self).get_context_data(**kwargs)
		context['schedule_list'] = Schedule.objects.filter(day=dia_actual, hour_start__lte=hora_actual, hour_end__gte=hora_actual)
		context['distributive_list'] = Distributive.objects.all()
		context['teacher_list'] = Teacher.objects.all()
		context['subject_list'] = Subject.objects.all()
		context['session_list'] = Internal.objects.filter(status=1)
		context['computer_list'] = Computer.objects.all()
		return context
	