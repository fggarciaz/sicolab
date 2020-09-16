# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.defaults import page_not_found

from apps.career.forms import CareerForm, SemesterForm
from apps.career.models import Career, Semester
from apps.career.serializers import SemesterSerializer

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph, Table, TableStyle, Image

import csv
# Create your views here.

#------ Vistas para Careers

class CareerList(ListView):
	#model = Career
	queryset = Career.objects.order_by('id_car')
	template_name = 'career/career_list.html'

class CareerCreate(CreateView):
	model = Career
	form_class = CareerForm
	template_name = 'career/career_form.html'
	success_url = reverse_lazy('career:career_listar')

class CareerUpdate(UpdateView):
	model = Career
	form_class = CareerForm
	template_name = 'career/career_form.html'
	success_url = reverse_lazy('career:career_listar')

class CareerDelete(DeleteView):
	model = Career
	template_name = 'career/career_delete.html'
	success_url = reverse_lazy('career:career_listar')

def CareerReport(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="Reporte_Carreras.pdf"'
	#response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	c.setTitle('Reporte de Carreras')

	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 22)
	c.drawString(4*cm, 27*cm,'SICOLAB')
	c.setFont('Helvetica', 14)
	c.drawString(4*cm, 26*cm,'Reporte de Carreras')
	img = Image('static/images/logo_carrera.jpg', width=2.5*cm, height=2.5*cm)
	img.drawOn(c, 17*cm, 25.6*cm)
	img = Image('static/images/sicolab_logo.png', width=3*cm, height=3*cm)
	img.drawOn(c, 0.8*cm, 25.2*cm)
	
	#Table header
	styles = getSampleStyleSheet()
	styleBH = styles['Normal']
	styleBH.alignment = TA_CENTER
	styleBH.fontSize = 10

	num = Paragraph('<b>#</b>', styleBH)
	car = Paragraph('<b>Carrera</b>', styleBH)
	sec = Paragraph('<b>Sección</b>', styleBH)

	data = []
	data.append([num, car, sec])

	#Table
	styleN = styles['BodyText']
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7
	high = 650
	
	for car in Career.objects.all():
		row = [car['id_car'], car['name_car'], car['section_car']]
		data.append(row)
		high = high - 18
	
	#Table size
	width, height = A4
	table = Table(data, colWidths=[2*cm, 10*cm, 7*cm])
	table.setStyle(TableStyle([
		('BACKGROUND', (0,0), (2,0), colors.lightblue),
		('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))
	
	#pdf size
	table.wrapOn(c, width, height)
	table.drawOn(c, 30, high)
	c.showPage

	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
	
def mi_error_404(request):
	nombre_template = '404.html'

	return page_not_found(request, template_name=nombre_template, status=404)

def mi_error_500(request):
	nombre_template = '500.html'

	return page_not_found(request, template_name=nombre_template, status=500)
	

#------ Vistas para Semesters

class SemesterList(ListView):
	#model = Semester
	queryset = Semester.objects.order_by('id_sem')
	template_name = 'career/semester_list.html'

class SemesterCreate	(CreateView):
	model = Semester
	form_class = SemesterForm
	template_name = 'career/semester_form.html'
	success_url = reverse_lazy('semester:semester_listar')

class SemesterUpdate(UpdateView):
	model = Semester
	form_class = SemesterForm
	template_name = 'career/semester_form.html'
	success_url = reverse_lazy('semester:semester_listar')

class SemesterDelete(DeleteView):
	model = Semester
	template_name = 'career/semester_delete.html'
	success_url = reverse_lazy('semester:semester_listar')

def SemesterReport(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="Reporte_Semestres.pdf"'
	#response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	c.setTitle('Reporte de Semestres')

	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 22)
	c.drawString(4*cm, 27*cm,'SICOLAB')
	c.setFont('Helvetica', 14)
	c.drawString(4*cm, 26*cm,'Reporte de Semestres')
	img = Image('static/images/logo_carrera.jpg', width=2.5*cm, height=2.5*cm)
	img.drawOn(c, 17*cm, 25.6*cm)
	img = Image('static/images/sicolab_logo.png', width=3*cm, height=3*cm)
	img.drawOn(c, 0.8*cm, 25.2*cm)
	
	#Table header
	styles = getSampleStyleSheet()
	styleBH = styles['Normal']
	styleBH.alignment = TA_CENTER
	styleBH.fontSize = 10

	num = Paragraph('<b>#</b>', styleBH)
	sem = Paragraph('<b>Semestre</b>', styleBH)
	par = Paragraph('<b>Paralelo</b>', styleBH)
	car = Paragraph('<b>Carrera</b>', styleBH)

	data = []
	data.append([num, sem, par, car])

	#Table
	styleN = styles['BodyText']
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7
	high = 650
	
	for seme in Semester.objects.all():
		row = [seme['id_sem'], seme['name_sem'], seme['parallel_sem'], seme['car']]
		data.append(row)
		high = high - 18
	
	#Table size
	width, height = A4
	table = Table(data, colWidths=[2*cm, 5*cm, 2*cm, 10*cm])
	table.setStyle(TableStyle([
		('BACKGROUND', (0,0), (3,0), colors.lightblue),
		('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))
	
	#pdf size
	table.wrapOn(c, width, height)
	table.drawOn(c, 30, high)
	c.showPage

	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
	

@csrf_exempt
def SemesterAPI_List(request):
	if request.method == 'GET':
			semester = Semester.objects.all()
			serializer = SemesterSerializer(semester, many=True)
			return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SemesterSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def SemesterAPI_Detail(request, pk):
	try:
		semester = Notify.objects.get(pk=pk)
		#hor= Horario.objd.get(idlad=semester.idlab, hora<horafin).firts()
		#response = HorarioSerializwe(hor)

	except Notify.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SemesterSerializer(semester)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SemesterSerializer(semester, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		semester.delete()
		return HttpResponse(status=204)