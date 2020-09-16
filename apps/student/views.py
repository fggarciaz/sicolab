# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import openpyxl
import math #LIBRERIAS AGREGADAS PARA LA VALIDACION
import re #LIBRERIAS AGREGADAS PARA LA VALIDACION

import json
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework.filters import SearchFilter

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from apps.student.forms import StudentForm, StudentUpdate
from apps.student.models import Student
from apps.student.serializers import StudentSerializer, StudentSerializer2

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework.mixins import UpdateModelMixin

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm, letter,landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph, Table, TableStyle, Image,SimpleDocTemplate

# Create your views here.

#------ Vistas para Students

class StudentList(ListView):
	#model = Student
	queryset = Student.objects.order_by('id_stu')
	template_name = 'student/student_list.html'

class StudentCreate(CreateView):
	model = Student
	form_class = StudentForm
	template_name = 'student/student_form.html'
	success_url = reverse_lazy('student:student_listar')

class StudentUpdate(UpdateView):
	model = Student
	form_class = StudentUpdate
	template_name = 'student/student_form.html'
	success_url = reverse_lazy('student:student_listar')

class StudentDelete(DeleteView):
	model = Student
	template_name = 'student/student_delete.html'
	success_url = reverse_lazy('student:student_listar')

class StudentAPI_List(generics.ListCreateAPIView):
	queryset = Student.objects.all().order_by('id_stu')
	serializer_class = StudentSerializer

#class StudentAPI_Detail(generics.UpdateAPIView, UpdateModelMixin):
class StudentAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	#serializer_class = StudentSerializer2
	serializer_class = StudentSerializer

def StudentReport(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="Reporte_Estudiantes.pdf"'
	#response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

	buffer = BytesIO()
	#c = canvas.Canvas(buffer, pagesize=A4
	c = canvas.Canvas(buffer, pagesize=A4)
	c.setTitle('Reporte de Estudiantes')
	

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
	ced = Paragraph('<b>Cédula</b>', styleBH)
	nom = Paragraph('<b>Estudiante</b>', styleBH)
	emai = Paragraph('<b>E-mail</b>', styleBH)
	est = Paragraph('<b>Estado</b>', styleBH)

	data = []
	data.append([num, ced, nom, emai, est])

	#Table
	styleN = styles['BodyText']
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7
	high = 650
	
	for stud in Student.objects.all():
		aux=""
		if stud.status_stu == 1:
			aux="Activo"
		else:
		  	aux="Inactivo"

		row = [stud['id_stu'], stud['dni_stu'], stud['names_stu'],stud['email_stu'], aux]
		data.append(row)
		high = high - 18
	
	#Table size
	width, height = A4
	table = Table(data, colWidths=[1*cm, 3*cm, 6.5*cm,6.5*cm, 2*cm])
	table.setStyle(TableStyle([
		('BACKGROUND', (0,0), (5,0), colors.lightblue),
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


#------ Vistas para Subject_Schedules

class Subject_StudentList(ListView):	
	queryset = Student.objects.order_by('id_stu')
	template_name = 'student/subject_student_list.html'

class Subject_StudentUpdate(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'student/subject_student_form.html'
	success_url = reverse_lazy('student:subject_student_listar')


#--------CLASES Y FUNCIONES PARA IMPORTAR

class StudentImport(TemplateView):
	#model = UploadForm
	#form_class = UploadForm
	template_name = 'student/student_import.html'
	#success_url = reverse_lazy('computer:computer_listar')


def studentCargarExcel(request):
	if request.method == 'POST':
		nombre_archivo = request.FILES.get('archivo')
		doc = openpyxl.load_workbook(nombre_archivo)
		nombres = doc.get_sheet_names()
		hoja = doc.get_sheet_by_name(nombres[0])
		datos = []
		lista = []
		error = ""
		cont = 0
		num = 2
		try:
			for filas in hoja.rows:
				if cont != 0:
					celda = "A"+repr(num)
					celdaE = "E"+repr(num)
					celdaD = "D"+repr(num)
					nro = hoja[celda].value
					nro2= hoja[celdaE].value
					nro3= hoja[celdaD].value
					if nro is None:
						break
					verificar_cedula(nro, celda)
					verificar_estado(nro2, celdaE)
					#validar_correo(nro3, celdaD)
					num = num + 1
				for columna in filas:
					if columna.value is not None:
						datos.append(columna.value)
					else:
						raise Exception('ERROR: existen celdas vacias')
				if len(datos)!=0:
						print datos
						lista.append(datos)
				datos = []
				cont = cont + 1
		except Exception as err:
			error = str(err)
		ruta = handle_uploaded_file(nombre_archivo)
		context = {'lista':lista, 'nombre_archivo': nombre_archivo, 'ruta':ruta, 'error': error}
		return render(request, 'student/student_list_excel.html', context)

def studentCargarBase(request):
	if request.method == 'GET':
		ruta = request.GET['enlace']
		doc = openpyxl.load_workbook('media/' + ruta)
		nombres = doc.get_sheet_names()
		hoja = doc.get_sheet_by_name(nombres[0])
		datos = []
		lista = []
		for filas in hoja.rows:
			for columna in filas:
				if columna.value is not None:
					datos.append(columna.value)	
			if len(datos)!=0:
					print "Al cargar en base de datos:"
					print datos
					lista.append(datos)
			datos = []
		x = 0
		estudiantesRegistrados = Student.objects.all()
		print len(lista)
		for fila in lista:
			if x == 0:
				x = x + 1
			else:
				if Student.objects.filter(dni_stu=fila[0]).count() == 0:
					Student.objects.create(dni_stu=fila[0], password_stu=fila[1], names_stu=fila[2], email_stu=fila[3], status_stu=fila[4])
		return HttpResponseRedirect(reverse('student:student_listar'))

def handle_uploaded_file(f):
    with open('media/' + str(f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return str(f.name)

#--------------------------------- VALIDACIONES :v ----------------------------

def verificar_cedula(nro, celda):
	l = len(nro)
	if l < 10:
		raise Exception('ERROR: en la celda '+celda+' existe una cedula incorrecta')

def verificar_estado(nro2, celdaE):
	if nro2 > 1:
		raise Exception('ERROR: en la celda '+celdaE+' existe un estado diferente de 1 o 0')