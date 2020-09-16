# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework import generics

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

#from apps.notify.forms import NotifyForm
from apps.notify.models import Notify
from apps.notify.serializers import NotifySerializer
# Create your views here.

class NotifyList(ListView):
 	model = Notify
 	queryset = Notify.objects.order_by('id')
 	template_name = 'notify/notify_list.html'

def update_notify(request):
    model = Notify
    queryset = Notify.objects.all()
    string = '{"staus":0}'
    return HttpResponse(string, content_type="application/json")

class NotifyAPI_List(generics.ListCreateAPIView):
	queryset = Notify.objects.all()
	serializer_class = NotifySerializer

class NotifyAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Notify.objects.all()
	serializer_class = NotifySerializer

@csrf_exempt
def NotifyAjax_List(request):
	if request.method == 'GET':
			notify = Notify.objects.all().filter(status=1)
			serializer = NotifySerializer(notify, many=True)
			return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = NotifySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
