# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.guest.forms import GuestForm
from apps.guest.models import Guest
from apps.lab.models import Lab
from apps.guest.serializers import GuestSerializer

import md5

# Create your views here.

class GuestList(ListView):
	queryset = Guest.objects.order_by('id_guest')
	template_name = 'guest/guest_list.html'

class GuestCreate(CreateView):
	model = Guest
	form_class = GuestForm
	template_name = 'guest/guest_create.html'
	success_url = reverse_lazy('guest:guest_listar')

class GuestUpdate(UpdateView):
	model = Guest
	form_class = GuestForm
	template_name = 'guest/guest_create.html'
	success_url = reverse_lazy('guest:guest_listar')

class GuestDelete(DeleteView):
	model = Guest
	template_name = 'guest/guest_delete.html'
	success_url = reverse_lazy('guest:guest_listar')

@csrf_exempt
def UsersDate(request):
	if request.method == 'POST':
		try:
			users= Guest()
			users.password_access=md5.new(request.POST.get('pass', None)).hexdigest()
			users.description=request.POST.get('description', None)
			users.start_time=request.POST.get('fini',None)+" "+request.POST.get('hini',None)
			users.finish_time=request.POST.get('fefin',None)+" "+request.POST.get('hfin',None)
			users.status=request.POST.get('status',None)
			users.lab_id=request.POST.get('laboratorio',None)
			users.save()
			#return HttpResponseRedirect(reverse('guest:guest_listar'))
		except Exception as err:
			error = str(err)
			print error
		return HttpResponseRedirect(reverse('guest:guest_listar'))


@csrf_exempt
def GuestAPI_List(request):
	if request.method == 'GET':
			guest = Guest.objects.all()
			serializer = GuestSerializer(guest, many=True)
			return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = GuestSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def GuestAPI_Detail(request, pk):
	try:
		guest = Notify.objects.get(pk=pk)
	except Notify.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = GuestSerializer(guest)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = GuestSerializer(guest, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		guest.delete()
		return HttpResponse(status=204)