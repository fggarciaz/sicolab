# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from apps.administrator.forms import AdministratorForm
from apps.administrator.models import Administrator
from apps.notify.models import Notify


# Create your views here.

#------ Vistas para Administrator
class AdministratorList(ListView):
	#model = Administrator
	queryset = Administrator.objects.order_by('id')
	template_name = 'administrator/administrator_list.html'

class AdministratorCreate(CreateView):
	model = Administrator
	form_class = AdministratorForm
	template_name = 'administrator/administrator_form.html'
	success_url = reverse_lazy('administrator:administrator_listar')

class AdministratorUpdate(UpdateView):
	model = Administrator
	form_class = AdministratorForm
	template_name = 'administrator/administrator_form.html'
	success_url = reverse_lazy('administrator:administrator_listar')

class AdministratorDelete(DeleteView):
	model = Administrator
	template_name = 'administrator/administrator_delete.html'
	success_url = reverse_lazy('administrator:administrator_listar')



class BuscarView(ListView):
	model = Notify
	template_name = 'administrator/administrator_form.html'
	context_object_name= 'notify'