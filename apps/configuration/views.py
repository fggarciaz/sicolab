# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, ListView

from apps.configuration.forms import ConfigurationForm
from apps.configuration.models import Configuration
from apps.configuration.serializers import ConfigurationSerializer

# Create your views here.

#------ Vistas para configuracion
class ConfigurationList(ListView):
	#model = Configuration
	queryset = Configuration.objects.order_by('id')
	template_name = 'configuration/configuration_list.html'

class ConfigurationUpdate(UpdateView):
	model = Configuration
	form_class = ConfigurationForm
	template_name = 'configuration/configuration_form.html'
	success_url = reverse_lazy('configuration:configuration_listar')

@csrf_exempt
def ConfigurationAPI_List(request):
	if request.method == 'GET':
			configuration = Configuration.objects.all()
			serializer = ConfigurationSerializer(configuration, many=True)
			return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ConfigurationSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ConfigurationAPI_Detail(request, pk):
	try:
		configuration = Configuration.objects.get(pk=pk)
	except Configuration.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ConfigurationSerializer(configuration)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ConfigurationSerializer(configuration, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		configuration.delete()
		return HttpResponse(status=204)