# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.distributive.forms import StageForm, DistributiveForm
from apps.distributive.models import Stage, Distributive
from apps.distributive.serializers import StageSerializer, DistributiveSerializer

from django.http import HttpResponse, HttpResponseRedirect
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm, letter,landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph, Table, TableStyle, Image,SimpleDocTemplate
from apps.career.models import Career, Semester
from apps.teacher.models import Teacher



#------ Vistas para Distributive

class DistributiveList(ListView):
	queryset = Distributive.objects.order_by('id_dist')
	template_name = 'distributive/distributive_list.html'

class DistributiveCreate(CreateView):
	model = Distributive
	form_class = DistributiveForm
	template_name = 'distributive/distributive_form.html'
	success_url = reverse_lazy('distributive:distributive_listar')

class DistributiveUpdate(UpdateView):
	model = Distributive
	form_class = DistributiveForm
	template_name = 'distributive/distributive_form.html'
	success_url = reverse_lazy('distributive:distributive_listar')

class DistributiveDelete(DeleteView):
	model = Distributive
	template_name = 'distributive/distributive_delete.html'
	success_url = reverse_lazy('distributive:distributive_listar')

class DistributiveAPI_List(generics.ListCreateAPIView):
	queryset = Distributive.objects.all()
	serializer_class = DistributiveSerializer

class DistributiveAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Distributive.objects.all()
	serializer_class = DistributiveSerializer

#------ Vistas para Stage

class StageList(ListView):
	queryset = Stage.objects.order_by('id_sta')
	template_name = 'distributive/stage_list.html'

class StageCreate(CreateView):
	model = Stage
	form_class = StageForm
	template_name = 'distributive/stage_form.html'
	success_url = reverse_lazy('stage:stage_listar')

class StageUpdate(UpdateView):
	model = Stage
	form_class = StageForm
	template_name = 'distributive/stage_form.html'
	success_url = reverse_lazy('stage:stage_listar')

class StageDelete(DeleteView):
	model = Stage
	template_name = 'distributive/stage_delete.html'
	success_url = reverse_lazy('stage:stage_listar')

class StageAPI_List(generics.ListCreateAPIView):
	queryset = Stage.objects.all()
	serializer_class = StageSerializer

class StageAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Stage.objects.all()
	serializer_class = StageSerializer

def pageHorizontal(c, buffer):
	#c = canvas.Canvas(buffer, pagesize=landscape(A4))
	c.setTitle('Reporte de Distributive')
	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 18)
	c.drawString( 9*cm,19*cm,'UNIVERSIDAD TÉCNICA DE MACHALA')
	c.setFont('Helvetica', 16)
	c.drawString( 9*cm,18.3*cm,'UNIDAD ACADÉMICA DE INGENIERIA CIVIL')
	c.setFont('Helvetica', 16)
	c.drawString( 9.2*cm,17.6*cm,'CARRERA DE INGENIERIA DE SISTEMAS')
	c.setFont('Helvetica', 14)
	c.drawString(12.2*cm, 16.8*cm,'Reporte de Distributivo')
	img = Image('static/images/logo_carrera.jpg', width=2.5*cm, height=2.5*cm)
	img.drawOn(c, 25.5*cm, 17.4*cm)
	img = Image('static/images/sicolab_logo.png', width=3*cm, height=3*cm)
	img.drawOn(c, 1.2*cm, 17*cm)
	return c

def pageVertical(c, buffer):
	#c = canvas.Canvas(buffer, pagesize=A4)
	c.setTitle('Reporte de Distributivo')
	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 18)
	c.drawString( 4.5*cm,28*cm,'UNIVERSIDAD TÉCNICA DE MACHALA')
	c.setFont('Helvetica', 16)
	c.drawString( 4.5*cm,27.4*cm,'UNIDAD ACADÉMICA DE INGENIERIA CIVIL')
	c.setFont('Helvetica', 16)
	c.drawString( 4.8*cm,26.8*cm,'CARRERA DE INGENIERIA DE SISTEMAS')
	c.setFont('Helvetica', 14)
	c.drawString(8*cm, 26*cm,'Reporte de Distributivo')
	img = Image('static/images/logo_carrera.jpg', width=2.5*cm, height=2.5*cm)
	img.drawOn(c, 17*cm, 26.4*cm)
	img = Image('static/images/sicolab_logo.png', width=3*cm, height=3*cm)
	img.drawOn(c, 0.8*cm, 26*cm)
	return c


def mostrarPagina(data, tamanio_columnas, c, width, height, high):
	#Table size
	#width, height = A4
	table = Table(data=data, colWidths=tamanio_columnas)
	table.setStyle(TableStyle([
		('BACKGROUND', (0,0), (5,0), colors.lightblue),
		('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))

	#pdf size
	table.wrapOn(c, width, height)
	table.drawOn(c, 30, high)

	c.showPage()


def DistributiveReport(request):
	if request.method == 'POST':
		periodo = request.POST['selectPeriodo'];
		semestre = request.POST['selectSemestre'];
		docente = request.POST['selectDocente'];
		print periodo + " " + semestre + " "+docente
		tamanio_columnas = []

		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'filename="Reporte_Distributivo.pdf"'

		buffer = BytesIO()
		c = None
		data = []
		#Table size
		width, height = A4
		#Table header
		styles = getSampleStyleSheet()
		styleBH = styles['Normal']
		styleBH.alignment = TA_CENTER
		styleBH.fontSize = 10

		#Table
		styleN = styles['BodyText']
		styleN.alignment = TA_CENTER
		styleN.fontSize = 7
		i = 0
		x = 0
		high = 650

		# periodo
		if periodo != "Todos" and semestre == "Todos" and docente == "Todos":
			c = canvas.Canvas(buffer, pagesize=landscape(A4))
			c = pageHorizontal(c, buffer)
			c.setFont('Helvetica', 12)
			nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
			c.drawString(1.2*cm, 16*cm,'Periodo: ' + nombre_periodo.name_sta)
			
			high = 430
			#Table size
			height, width  = A4
			
			num = Paragraph('<b>#</b>', styleBH)
			sem = Paragraph('<b>Semestre</b>', styleBH)
			doc = Paragraph('<b>Docente</b>', styleBH)
			asi = Paragraph('<b>Asignatura</b>', styleBH)

			tamanio_columnas = [1*cm, 8.4*cm, 9*cm, 9*cm]

			data.append([num, sem, doc, asi])
			for stud in Distributive.objects.filter(sta=periodo):
				height, width  = A4
				i = i + 1
				x = x + 1
				row = [i,stud['sem'], stud['tea'], stud['sub']]
				data.append(row)
				high = high - 18

				if x == 22:
					x = 0
					mostrarPagina(data, tamanio_columnas, c, width, height, high)
					high = 430
					data = []
					data.append([num, sem, doc, asi])

			if x != 22:
				c = pageHorizontal(c, buffer)
				c.setFont('Helvetica', 12)
				nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
				c.drawString(1.2*cm, 16*cm,'Periodo: ' + nombre_periodo.name_sta)
				mostrarPagina(data, tamanio_columnas, c, width, height, high)

		# semestre
		if periodo == "Todos" and semestre != "Todos" and docente == "Todos":
			c = canvas.Canvas(buffer, pagesize=landscape(A4))
			c = pageHorizontal(c, buffer)

			c.setFont('Helvetica', 11)
			nombre_semestre = Semester.objects.get(id_sem=semestre)
			c.drawString(1.2*cm, 16.2*cm,'Carrera: ' + nombre_semestre.car.name_car)
			c.setFont('Helvetica', 11)
			c.drawString(1.2*cm, 15.7*cm,'Semestre: ' + nombre_semestre.name_sem + " " + nombre_semestre.parallel_sem)
			high = 420
			#Table size
			height, width  = A4
			
			num = Paragraph('<b>#</b>', styleBH)
			per = Paragraph('<b>Periodo</b>', styleBH)
			doc = Paragraph('<b>Docente</b>', styleBH)
			asi = Paragraph('<b>Asignatura</b>', styleBH)

			tamanio_columnas = [1*cm, 3*cm, 10*cm,13*cm]

			data.append([num, per, doc, asi])
			for stud in Distributive.objects.filter(sem=semestre):
				i = i + 1
				x = x + 1
				row = [i,stud['sta'], stud['tea'], stud['sub']]
				data.append(row)
				high = high - 18

				if x == 22:
					x = 0
					mostrarPagina(data, tamanio_columnas, c, width, height, high)
					high = 420
					data = []
					data.append([num, per, doc, asi])

			if x != 22:
				c = pageHorizontal(c, buffer)
				c.setFont('Helvetica', 11)
				nombre_semestre = Semester.objects.get(id_sem=semestre)
				c.drawString(1.2*cm, 16.2*cm,'Carrera: ' + nombre_semestre.car.name_car)
				c.setFont('Helvetica', 11)
				c.drawString(1.2*cm, 15.7*cm,'Semestre: ' + nombre_semestre.name_sem + " " + nombre_semestre.parallel_sem)
				mostrarPagina(data, tamanio_columnas, c, width, height, high)
			


		# periodo 	semestre
		if periodo != "Todos" and semestre != "Todos" and docente == "Todos":
			c = canvas.Canvas(buffer, pagesize=A4)
			c = pageVertical(c, buffer)
			high = 660
			
			c.setFont('Helvetica', 11)
			nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
			c.drawString(1*cm, 25.2*cm,'Periodo: ' + nombre_periodo.name_sta)
			nombre_semestre = Semester.objects.get(id_sem=semestre)
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 24.7*cm,'Carrera: ' + str(nombre_semestre.car.name_car))
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 24.2*cm,'Semestre: ' + str(nombre_semestre.name_sem) + ' ' + str(nombre_semestre.parallel_sem))

			num = Paragraph('<b>#</b>', styleBH)
			doc = Paragraph('<b>Docente</b>', styleBH)
			asi = Paragraph('<b>Asignatura</b>', styleBH)
			tamanio_columnas = [1.4*cm, 7.5*cm, 10.1*cm]

			data.append([num, doc, asi])

			for stud in Distributive.objects.filter(sta=periodo, sem=semestre):
				i = i + 1
				x = x + 1
				row = [i, stud['tea'], stud['sub']]
				data.append(row)
				high = high - 18

			
				if x == 35:
					x = 0
					mostrarPagina(data, tamanio_columnas, c, width, height, high)
					high = 660
					data = []
					data.append([num, doc, asi])

			if x != 35:
				c = pageVertical(c, buffer)
				c.setFont('Helvetica', 11)
				nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
				c.drawString(1*cm, 25.2*cm,'Periodo: ' + nombre_periodo.name_sta)
				nombre_semestre = Semester.objects.get(id_sem=semestre)
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 24.7*cm,'Carrera: ' + str(nombre_semestre.car.name_car))
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 24.2*cm,'Semestre: ' + str(nombre_semestre.name_sem) + ' ' + str(nombre_semestre.parallel_sem))
				mostrarPagina(data, tamanio_columnas, c, width, height, high)


		#periodo 	semestre 	docente
		if periodo != "Todos" and semestre != "Todos" and docente != "Todos":
			c = canvas.Canvas(buffer, pagesize=A4)
			c = pageVertical(c, buffer)
			high = 660
			
			c.setFont('Helvetica', 11)
			nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
			c.drawString(1*cm, 25.7*cm,'Periodo: ' + nombre_periodo.name_sta)
			nombre_semestre = Semester.objects.get(id_sem=semestre)
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 25.2*cm,'Carrera: ' + str(nombre_semestre.car.name_car))
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 24.7*cm,'Semestre: ' + str(nombre_semestre.name_sem) + ' ' + str(nombre_semestre.parallel_sem))
			nombre_docente = Teacher.objects.get(id_tea=docente)
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 24.2*cm,'Docente: ' + str(nombre_docente.names_tea))

			tamanio_columnas = [2*cm, 17*cm]

			num = Paragraph('<b>#</b>', styleBH)
			asi = Paragraph('<b>Asignatura</b>', styleBH)
			data.append([num, asi])
			for stud in Distributive.objects.filter(sta=periodo, sem=semestre, tea=docente):
				i = i + 1
				x = x + 1
				row = [i, stud['sub']]
				data.append(row)
				high = high - 18

				if x == 35:
					x = 0
					mostrarPagina(data, tamanio_columnas, c, width, height, high)
					high = 660
					data = []
					data.append([num, asi])

			if x != 35:
				c = pageVertical(c, buffer)
				c.setFont('Helvetica', 11)
				nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
				c.drawString(1*cm, 25.7*cm,'Periodo: ' + nombre_periodo.name_sta)
				nombre_semestre = Semester.objects.get(id_sem=semestre)
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 25.2*cm,'Carrera: ' + str(nombre_semestre.car.name_car))
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 24.7*cm,'Semestre: ' + str(nombre_semestre.name_sem) + ' ' + str(nombre_semestre.parallel_sem))
				nombre_docente = Teacher.objects.get(id_tea=docente)
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 24.2*cm,'Docente: ' + str(nombre_docente.names_tea))
				mostrarPagina(data, tamanio_columnas, c, width, height, high)



		#periodo docente
		if periodo != "Todos" and semestre == "Todos" and docente != "Todos":
			c = canvas.Canvas(buffer, pagesize=A4)
			c = pageVertical(c, buffer)
			high = 680
			
			c.setFont('Helvetica', 11)
			nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
			c.drawString(1*cm, 25.7*cm,'Periodo: ' + nombre_periodo.name_sta)
			nombre_docente = Teacher.objects.get(id_tea=docente)
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 25.2*cm,'Docente: ' + str(nombre_docente.names_tea))

			num = Paragraph('<b>#</b>', styleBH)
			sem = Paragraph('<b>Semestre</b>', styleBH)
			asi = Paragraph('<b>Asignatura</b>', styleBH)
			tamanio_columnas = [1*cm, 8*cm, 10*cm]

			data.append([num, sem, asi])
			for stud in Distributive.objects.filter(sta=periodo, tea=docente):
				i = i + 1
				x = x + 1
				row = [i,stud['sem'], stud['sub']]
				data.append(row)
				high = high - 18

		
				if x == 35:
					x = 0
					mostrarPagina(data, tamanio_columnas, c, width, height, high)
					high = 680
					data = []
					data.append([num, sem, asi])

			if x != 35:
				c = pageVertical(c, buffer)
				c.setFont('Helvetica', 11)
				nombre_periodo = nombre_periodo = Stage.objects.get(id_sta=periodo)
				c.drawString(1*cm, 25.7*cm,'Periodo: ' + nombre_periodo.name_sta)
				nombre_docente = Teacher.objects.get(id_tea=docente)
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 25.2*cm,'Docente: ' + str(nombre_docente.names_tea))
				mostrarPagina(data, tamanio_columnas, c, width, height, high)

		#semestre 	docente
		if periodo == "Todos" and semestre != "Todos" and docente != "Todos":
			c = canvas.Canvas(buffer, pagesize=A4)
			c = pageVertical(c, buffer)
			high = 670
			
			nombre_semestre = Semester.objects.get(id_sem=semestre)
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 25.7*cm,'Carrera: ' + str(nombre_semestre.car.name_car))
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 25.2*cm,'Semestre: ' + str(nombre_semestre.name_sem) + ' ' + str(nombre_semestre.parallel_sem))
			nombre_docente = Teacher.objects.get(id_tea=docente)
			c.setFont('Helvetica', 11)
			c.drawString(1*cm, 24.7*cm,'Docente: ' + str(nombre_docente.names_tea))

			num = Paragraph('<b>#</b>', styleBH)
			per = Paragraph('<b>Periodo</b>', styleBH)
			asi = Paragraph('<b>Asignatura</b>', styleBH)

			tamanio_columnas = [1*cm, 5*cm, 13*cm]
			data.append([num, per, asi])

			for stud in Distributive.objects.filter(sem=semestre, tea=docente):
				i = i + 1
				x = x + 1
				row = [i, stud['sta'], stud['sub']]
				data.append(row)
				high = high - 18

				if x == 35:
					x = 0
					mostrarPagina(data, tamanio_columnas, c, width, height, high)
					high = 670
					data = []
					data.append([num, per, asi])

			if x != 35:
				c = pageVertical(c, buffer)
				nombre_semestre = Semester.objects.get(id_sem=semestre)
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 25.7*cm,'Carrera: ' + str(nombre_semestre.car.name_car))
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 25.2*cm,'Semestre: ' + str(nombre_semestre.name_sem) + ' ' + str(nombre_semestre.parallel_sem))
				nombre_docente = Teacher.objects.get(id_tea=docente)
				c.setFont('Helvetica', 11)
				c.drawString(1*cm, 24.7*cm,'Docente: ' + str(nombre_docente.names_tea))

				mostrarPagina(data, tamanio_columnas, c, width, height, high)

		#docente
		if periodo == "Todos" and semestre == "Todos" and docente != "Todos":
			c = canvas.Canvas(buffer, pagesize=landscape(A4))
			c = pageHorizontal(c, buffer)

			c.setFont('Helvetica', 12)
			nombre_docente = Teacher.objects.get(id_tea=docente)
			c.drawString(1.2*cm, 16*cm,'Docente: ' + str(nombre_docente.names_tea))
			high = 430
			i = 0
			x = 0
			#Table size
			height, width  = A4
			tamanio_columnas = [1*cm, 4*cm, 8*cm, 14*cm]

			num = Paragraph('<b>#</b>', styleBH)
			per = Paragraph('<b>Periodo</b>', styleBH)
			sem = Paragraph('<b>Semestre</b>', styleBH)
			asi = Paragraph('<b>Asignatura</b>', styleBH)

			data.append([num, per, sem, asi])
			for stud in Distributive.objects.filter(tea=docente):
				i = i + 1
				x = x + 1
				row = [i,stud['sta'], stud['sem'],stud['sub']]
				data.append(row)
				high = high - 18

			
				if x == 22:
						print "Entre i: " + str(i)
						x = 0
						mostrarPagina(data, tamanio_columnas, c, width, height, high)
						high = 430
						data = []
						data.append([num, per, sem, asi])

			if x != 22:
				c = pageHorizontal(c, buffer)
				c.setFont('Helvetica', 12)
				nombre_docente = Teacher.objects.get(id_tea=docente)
				c.drawString(1.2*cm, 16*cm,'Docente: ' + str(nombre_docente.names_tea))
				mostrarPagina(data, tamanio_columnas, c, width, height, high)
		
		
		
		c.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response