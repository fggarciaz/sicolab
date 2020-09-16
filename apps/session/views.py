# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics

from django.shortcuts import render
from django.views.generic import ListView

from apps.student.models import Student
from apps.session.models import Internal, External
from apps.session.serializers import InternalSerializer, ExternalSerializer

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm, letter,landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph, Table, TableStyle, Image,SimpleDocTemplate
from django.http import HttpResponse
from reportlab.lib.units import inch

# Create your views Internal
class InternalList(ListView):
	queryset = Internal.objects.order_by('id_inter')
	template_name = 'internal/internal _list.html'

class InternalAPI_List(generics.ListCreateAPIView):
	queryset = Internal.objects.all()
	serializer_class = InternalSerializer

class InternalAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Internal.objects.all()
	serializer_class = InternalSerializer

def InternalReport(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="Reporte_Session_Interna.pdf"'
	#response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

	buffer = BytesIO()
	#c = canvas.Canvas(buffer, pagesize=A4
	c = canvas.Canvas(buffer, pagesize=landscape(A4))
	c.setTitle('Reporte de las Sesiones Internas')

	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 22)
	c.drawString(4*cm, 18*cm,'SICOLAB')
	c.setFont('Helvetica', 14)
	c.drawString(4*cm, 17*cm,'Reporte de Carreras')
	img = Image('static/images/logo_carrera.jpg', width=2.5*cm, height=2.5*cm)
	img.drawOn(c, 25*cm, 16.6*cm)
	img = Image('static/images/sicolab_logo.png', width=3*cm, height=3*cm)
	img.drawOn(c, 0.8*cm, 16.2*cm)
	
	#Table header
	styles = getSampleStyleSheet()
	styleBH = styles['Normal']
	styleBH.alignment = TA_CENTER
	styleBH.fontSize = 10

	num = Paragraph('<b>#</b>', styleBH)
	fi = Paragraph('<b>Fecha Inicio</b>', styleBH)
	ff = Paragraph('<b>Fecha Fin</b>', styleBH)
	fs = Paragraph('<b>Fin Sesión</b>', styleBH)
	est = Paragraph('<b>Estado</b>', styleBH)
	tip = Paragraph('<b>Tipo Usuario</b>', styleBH)
	nom = Paragraph('<b>Usuario</b>', styleBH)
	maq = Paragraph('<b>Computadora</b>', styleBH)
	
	data = []
	data.append([num,fi,ff,fs,est,tip,nom,maq])

	#Table
	styleN = styles['BodyText']
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7
	high = 420
	
	for inte in Internal.objects.all():
		status=""
		if inte.status == 1:
			status="Activo"
		else:
		  	status="Inactivo"
		tipo=""
		usu=""
		if inte.type_user == "S":
			tipo="Estudiante"
			for est in Student.objects.all():
				if est.id_stu == inte.id_user:
					usu=est.names_stu
		else:
		  	tipo="Profesor"
		  	for profe in Teacher.objects.all():
				if profe.id == inte.id_user:
					usu=profe.names_tea
		compu=inte.comp.name_comp 
		fini=str(inte.start_time).replace("+00:00","")
		ffin=str(inte.finish_time).replace("+00:00","")
		fsess=str(inte.finish_session).replace("+00:00","")

		row = [inte['id_inter'],fini,ffin,fsess,status,tipo,usu, compu]
		data.append(row)
		high = high - 18
	
	#Table size
	width, height = A4
	table = Table(data, colWidths=[1*cm, 4*cm, 4*cm,4*cm, 1.6*cm, 2.4*cm,7*cm, 2.8*cm])
	table.setStyle(TableStyle([
		('BACKGROUND', (0,0), (8,0), colors.lightblue),
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


# @csrf_exempt
# def InternalAPI_List(request):
# 	if request.method == 'GET':
# 			internal = Internal.objects.all()
# 			serializer = InternalSerializer(internal, many=True)
# 			return JsonResponse(serializer.data, safe=False)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = InternalSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def InternalAPI_Detail(request, pk):
# 	try:
# 		internal = Internal.objects.get(pk=pk)
# 	except Internal.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = InternalSerializer(internal)
# 		return JsonResponse(serializer.data)

# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = InternalSerializer(internal, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data)
# 		return JsonResponse(serializer.errors, status=400)

# 	elif request.method == 'DELETE':
# 		internal.delete()
# 		return HttpResponse(status=204)

# Create your views External

class ExternalList(ListView):
	queryset = External.objects.order_by('id_exter')
	template_name = 'external/external _list.html'

class ExternalAPI_List(generics.ListCreateAPIView):
	queryset = External.objects.all()
	serializer_class = ExternalSerializer

class ExternalAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = External.objects.all()
	serializer_class = ExternalSerializer

def ExternalReport(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="Reporte_Session_Externa.pdf"'
	#response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

	buffer = BytesIO()
	#c = canvas.Canvas(buffer, pagesize=A4
	c = canvas.Canvas(buffer, pagesize=landscape(A4))
	c.setTitle('Reporte de las Sesiones Externas')
	
	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 22)
	c.drawString(4*cm, 18*cm,'SICOLAB')
	c.setFont('Helvetica', 14)
	c.drawString(4*cm, 17*cm,'Reporte de Carreras')
	img = Image('static/images/logo_carrera.jpg', width=2.5*cm, height=2.5*cm)
	img.drawOn(c, 25*cm, 16.6*cm)
	img = Image('static/images/sicolab_logo.png', width=3*cm, height=3*cm)
	img.drawOn(c, 0.8*cm, 16.2*cm)
	
	#Table header
	styles = getSampleStyleSheet()
	styleBH = styles['Normal']
	styleBH.alignment = TA_CENTER
	styleBH.fontSize = 10

	num = Paragraph('<b>#</b>', styleBH)
	nus = Paragraph('<b>Nombre Usuario</b>', styleBH)
	fi = Paragraph('<b>Fecha Inicio</b>', styleBH)
	ff = Paragraph('<b>Fecha Fin</b>', styleBH)
	fs = Paragraph('<b>Fin Sesión</b>', styleBH)
	est = Paragraph('<b>Estado</b>', styleBH)
	tip = Paragraph('<b>Descripcion</b>', styleBH)
	maq = Paragraph('<b>Computadora</b>', styleBH)
	
	data = []
	data.append([num,nus,fi,ff,fs,est,tip,maq])

	#Table
	styleN = styles['BodyText']
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7
	high = 425
	
	for exte in External.objects.all():
		status=""
		if exte.status == 1:
			status="Activo"
		else:
		  	status="Inactivo"
		
		des=exte.guest.description
		compu=exte.comp.name_comp

		fini=str(exte.start_time).replace("+00:00","")
		ffin=str(exte.finish_time).replace("+00:00","")
		fsess=str(exte.finish_session).replace("+00:00","")

		row = [exte['id_exter'],exte['name_user'],fini,ffin,fsess,status,des,compu ]
		data.append(row)
		#high = high - 18
	
	#Table size
	width, height = A4
	table = Table(data, colWidths=[1*cm, 4.5*cm, 4.7*cm,4.7*cm, 4.7*cm, 1.7*cm,4*cm, 2.9*cm])
	table.setStyle(TableStyle([
		('BACKGROUND', (0,0), (8,0), colors.lightblue),
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

# @csrf_exempt
# def ExternalAPI_List(request):
# 	if request.method == 'GET':
# 			external = External.objects.all()
# 			serializer = ExternalSerializer(external, many=True)
# 			return JsonResponse(serializer.data, safe=False)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = ExternalSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def ExternalAPI_Detail(request, pk):
# 	try:
# 		external = External.objects.get(pk=pk)
# 	except External.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = ExternalSerializer(external)
# 		return JsonResponse(serializer.data)

# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = ExternalSerializer(external, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data)
# 		return JsonResponse(serializer.errors, status=400)

# 	elif request.method == 'DELETE':
# 		external.delete()
# 		return HttpResponse(status=204)