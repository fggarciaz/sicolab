# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import openpyxl
#import time
from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from rest_framework import generics

from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView


from apps.schedule.forms import ScheduleForm
from apps.schedule.models import Schedule
from apps.lab.models import Lab
from apps.distributive.models import Distributive
from apps.schedule.serializers import ScheduleSerializer

#Librerias para pdf
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from datetime import datetime

from apps.distributive.models import Stage, Distributive
from apps.lab.models import Lab


# Create your views here.

class ScheduleList(ListView):
	#model = Schedule
	queryset = Schedule.objects.order_by('id_sched')
	template_name = 'schedule/schedule_list.html'

class ScheduleCreate(CreateView):
	model = Schedule
	form_class = ScheduleForm
	template_name = 'schedule/schedule_form.html'
	success_url = reverse_lazy('schedule:schedule_listar')

class ScheduleUpdate(UpdateView):
	model = Schedule
	form_class = ScheduleForm
	template_name = 'schedule/schedule_form.html'
	success_url = reverse_lazy('schedule:schedule_listar')

class ScheduleDelete(DeleteView):
	model = Schedule
	template_name = 'schedule/schedule_delete.html'
	success_url = reverse_lazy('schedule:schedule_listar')

class ScheduleAPI_List(generics.ListCreateAPIView):
	#hora_actual = time.strftime("%H:%M:%S")	
	#dia_actual = time.strftime("%w")	
	#queryset = Schedule.objects.filter(day=dia_actual, hour_start__lte=hora_actual, hour_end__gte=hora_actual)
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer

class ScheduleAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer

def ScheduleReport(request):
	if request.method == 'POST':
		periodo = request.POST['selectPeriodo'];
		docente = request.POST['selectDocente'];

		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'filename="Reporte_Horarios.pdf"'

		styles = getSampleStyleSheet()

		styleN = styles["BodyText"]
		styleN.alignment = TA_LEFT
		styleN.fontSize = 6.2

		styleBH = styles["Normal"]
		styleBH.alignment = TA_CENTER
		styleBH.fontSize = 10
		styleBH.color = colors.white


		img= (Image('static/images/sicolab_carr.png', width=25*cm, height=4.7*cm))	
	   
		hora= Paragraph("\nHora\n", styleBH)
		lunes= Paragraph("\nLunes\n", styleBH)
		martes= Paragraph("\nMartes\n", styleBH)
		miercoles= Paragraph("\nMiércoles\n", styleBH)
		jueves= Paragraph("\nJueves\n", styleBH)
		viernes= Paragraph("\nViernes\n", styleBH)



		arr_i=["07:00:00", "08:00:00", "09:00:00", "10:00:00" ,"11:00:00", "12:00:00"]
		arr_f=["08:00:00", "09:00:00", "10:00:00" ,"11:00:00", "12:00:00",  "13:00:00"]

		estilos_tabla=[                    
			('GRID', (0, 1), (-1, -1), 0.5, colors.transparent),
			('BOX', (0, 0), (-1, -1), 2, colors.gray),
			('BACKGROUND', (0, 0), (12, 0), colors.lightblue),
			('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
			('FONTSIZE', (0, 0), (-1, 0), 12),
			('FONTSIZE', (0, 1), (-1, 1), 7.5),
			('FONTSIZE', (0, 2), (-1, 2), 7.5),  
			('FONTSIZE', (0, 3), (-1, 3), 7.5), 
			('FONTSIZE', (0, 4), (-1, 4), 7.5), 
			('FONTSIZE', (0, 5), (-1, 5), 7.5), 
			('FONTSIZE', (0, 6), (-1, 6), 7.5),
			('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			('ALIGN', (0, 1), (-1, 1), 'CENTER'),
			('ALIGN', (0, 2), (-1, 2), 'CENTER'), 
			('ALIGN', (0, 3), (-1, 3), 'CENTER'), 
			('ALIGN', (0, 4), (-1, 4), 'CENTER'), 
			('ALIGN', (0, 5), (-1, 5), 'CENTER'), 
			('ALIGN', (0, 6), (-1, 6), 'CENTER'),  
			]

		p = canvas.Canvas(response,  pagesize=landscape(A4))
		listaLaboratorios = []
		listaVerificacion = []
		duplicado = False
		numero_periodo = 0

		if periodo != "Todos" and docente == "Todos":
			per = Stage.objects.get(id_sta=periodo)
			dist = Distributive.objects.filter(sta=per.id_sta)
			lista = []
			for d in dist:
				sche = Schedule.objects.filter(dist=d.id_dist)
				if len(sche) > 0:
					for x in sche:
						lista.append(x)

			for ob in lista:
				if len(listaVerificacion)==0:
					
					listaVerificacion.append(ob.lab)
				else:
					for i in listaVerificacion:
						if i.id_lab == ob.lab.id_lab:
							duplicado = True
							break
				if duplicado == False:
					listaVerificacion.append(ob.lab)
					listaLaboratorios.append(ob.lab)
				duplicado = False

			for lab in listaLaboratorios:

				img.drawOn(p , 2.2*cm, 15.5*cm)
				p.setFont('Helvetica', 15)
				p.drawString(10*cm, 15*cm, lab.name_lab)
				width, height = A4	

				datos = [[hora, lunes, martes, miercoles, jueves, viernes]]

				for i in range(0,6):

					row= []

					row= ["\n"+arr_i[i]+"\n"+arr_f[i]+"\n", "\n----------\n", "\n----------\n", "\n----------\n", "\n----------\n", "\n----------\n"]

					#print row

					for j in range(1,6):

						#print j

		  				h_resp = None

						#for sch in Schedule.objects.all():
						for sch in lista:

							if lab.id_lab == sch.lab_id:
								
								(h_i, m_i, s_i) = arr_i[i].split(':') 
								(h_f, m_f, s_f) = arr_f[i].split(':') 

								strin= str(sch.dist)
								array = strin.split('|')

								(h_a_i, m_a_i, s_a_i) = str(sch.hour_start).split(':') 
								(h_a_f, m_a_i, s_a_i) = str(sch.hour_end).split(':')

								if ((sch.day == str(j)) and (h_i >= h_a_i) and (h_f <= h_a_f)):
									#print str(sch.hour_start) + "  "+ str(sch.hour_end)
									h_resp = "\n"+array[2]+"\n"+array[3]+"\n"+array[0]
									#print array[3]+"\n"+array[2]
									row[j]= h_resp
						#print row
					datos.append(row)

				tabla = Table(data=datos,  style= estilos_tabla  , colWidths=[50, 135, 135, 135, 135, 135],
							rowHeights=[30, 45, 45, 45, 45, 45, 45])
				tabla.Align = "CENTER"
				tabla.wrapOn(p, width, height)
				tabla.drawOn(p,  2*cm, 100)
				p.setFont('Helvetica', 11)
				p.drawString(8*cm, 1.3*cm, "___________________________")
				#p.drawString(7.5*cm, 1.3*cm, "Ing. Ronald Christopher Elizalde López")
				p.drawString(9*cm, 0.8*cm, "Administrador de TIC")
				p.drawString(16*cm, 1.3*cm, "__________________________")
				#p.drawString(16.01*cm, 1.3*cm, "Ing. Jimmy Rolando Molina Rios")
				p.drawString(16.6*cm, 0.8*cm, "Coordinador de la Carrera")
				
				p.showPage()

		if periodo != "Todos" and docente != "Todos":
			per = Stage.objects.get(id_sta=periodo)
			dist = Distributive.objects.filter(sta=per.id_sta)
			lista = []
			for d in dist:
				sche = Schedule.objects.filter(dist=d.id_dist, lab=docente)
				if len(sche) > 0:
					for x in sche:
						lista.append(x)

			for ob in lista:
				#lab = Lab.objects.get(id_lab=ob.lab.id_lab)
				if len(listaVerificacion)==0:
					
					listaVerificacion.append(ob.lab)
				else:
					for i in listaVerificacion:
						if i.id_lab == ob.lab.id_lab:
							duplicado = True
							break
							
				if duplicado == False:
					listaVerificacion.append(ob.lab)
					listaLaboratorios.append(ob.lab)
				duplicado = False

			for lab in listaLaboratorios:

				img.drawOn(p , 2.2*cm, 15.5*cm)
				p.setFont('Helvetica', 15)
				p.drawString(10*cm, 15*cm, lab.name_lab)
				width, height = A4	

				datos = [[hora, lunes, martes, miercoles, jueves, viernes]]

				for i in range(0,6):

					row= []

					row= ["\n"+arr_i[i]+"\n"+arr_f[i]+"\n", "\n----------\n", "\n----------\n", "\n----------\n", "\n----------\n", "\n----------\n"]

					#print row

					for j in range(1,6):
						#print j
		  				h_resp = None
						#for sch in Schedule.objects.all():
						for sch in lista:

							if lab.id_lab == sch.lab_id:
								
								(h_i, m_i, s_i) = arr_i[i].split(':') 
								(h_f, m_f, s_f) = arr_f[i].split(':') 

								strin= str(sch.dist)
								array = strin.split('|')

								(h_a_i, m_a_i, s_a_i) = str(sch.hour_start).split(':') 
								(h_a_f, m_a_i, s_a_i) = str(sch.hour_end).split(':')

								if ((sch.day == str(j)) and (h_i >= h_a_i) and (h_f <= h_a_f)):
									#print str(sch.hour_start) + "  "+ str(sch.hour_end)
									h_resp = "\n"+array[2]+"\n"+array[3]+"\n"+array[0]
									#print array[3]+"\n"+array[2]
									row[j]= h_resp
						#print row
					datos.append(row)

				tabla = Table(data=datos,  style= estilos_tabla  , colWidths=[50, 135, 135, 135, 135, 135],
							rowHeights=[30, 45, 45, 45, 45, 45, 45])
				tabla.Align = "CENTER"
				tabla.wrapOn(p, width, height)
				tabla.drawOn(p,  2*cm, 100)
				p.setFont('Helvetica', 11)
				p.drawString(8*cm, 2*cm, "___________________________")
				p.drawString(7.5*cm, 1.3*cm, "Ing. Ronald Christopher Elizalde López")
				p.drawString(9*cm, 0.8*cm, "Administrador de TIC")
				p.drawString(16*cm, 2*cm, "__________________________")
				p.drawString(16.01*cm, 1.3*cm, "Ing. Jimmy Rolando Molina Rios")
				p.drawString(16.6*cm, 0.8*cm, "Coordinador de la Carrera")
				
				p.showPage()

		if periodo == "Todos" and docente != "Todos":
			
			for st in Stage.objects.all():

				#per = Stage.objects.get(id_sta=st.id_dist)
				dist = Distributive.objects.filter(sta=st.id_sta)
				lista = []
				for d in dist:
					sche = Schedule.objects.filter(dist=d.id_dist, lab=docente)
					if len(sche) > 0:
						for x in sche:
							lista.append(x)

				for ob in lista:
					if len(listaVerificacion)==0:
						
						listaVerificacion.append(ob.lab)
					else:
						for i in listaVerificacion:
							if i.id_lab == ob.lab.id_lab:
								duplicado = True
								break
								
					if duplicado == False:
						listaVerificacion.append(ob.lab)
						listaLaboratorios.append(ob.lab)
					duplicado = False

				for lab in listaLaboratorios:

					img.drawOn(p , 2.2*cm, 15.5*cm)
					p.setFont('Helvetica', 15)
					p.drawString(13*cm, 15.6*cm, 'Periodo ' + str(st.name_sta))
					p.setFont('Helvetica', 15)
					p.drawString(10*cm, 15*cm, lab.name_lab)
					width, height = A4	

					datos = [[hora, lunes, martes, miercoles, jueves, viernes]]

					for i in range(0,6):

						row= []

						row= ["\n"+arr_i[i]+"\n"+arr_f[i]+"\n", "\n----------\n", "\n----------\n", "\n----------\n", "\n----------\n", "\n----------\n"]

						#print row

						for j in range(1,6):

							#print j

			  				h_resp = None

							#for sch in Schedule.objects.all():
							for sch in lista:

								if lab.id_lab == sch.lab_id:
									
									(h_i, m_i, s_i) = arr_i[i].split(':') 
									(h_f, m_f, s_f) = arr_f[i].split(':') 

									strin= str(sch.dist)
									array = strin.split('|')

									(h_a_i, m_a_i, s_a_i) = str(sch.hour_start).split(':') 
									(h_a_f, m_a_i, s_a_i) = str(sch.hour_end).split(':')

									if ((sch.day == str(j)) and (h_i >= h_a_i) and (h_f <= h_a_f)):
										#print str(sch.hour_start) + "  "+ str(sch.hour_end)
										h_resp = "\n"+array[2]+"\n"+array[3]+"\n"+array[0]
										#print array[3]+"\n"+array[2]
										row[j]= h_resp
							#print row
						datos.append(row)

					tabla = Table(data=datos,  style= estilos_tabla  , colWidths=[50, 135, 135, 135, 135, 135],
								rowHeights=[30, 45, 45, 45, 45, 45, 45])
					tabla.Align = "CENTER"
					tabla.wrapOn(p, width, height)
					tabla.drawOn(p,  2*cm, 100)
					p.setFont('Helvetica', 11)
					p.drawString(8*cm, 2*cm, "___________________________")
					p.drawString(7.5*cm, 1.3*cm, "Ing. Ronald Christopher Elizalde López")
					p.drawString(9*cm, 0.8*cm, "Administrador de TIC")
					p.drawString(16*cm, 2*cm, "__________________________")
					p.drawString(16.01*cm, 1.3*cm, "Ing. Jimmy Rolando Molina Rios")
					p.drawString(16.6*cm, 0.8*cm, "Coordinador de la Carrera")
					
					p.showPage()
				listaVerificacion = []
				listaLaboratorios = []




		
		
		p.save()

		return response


#--------CLASES Y FUNCIONES PARA IMPORTAR TEACHER

class ScheduleImport(TemplateView):
	#model = UploadForm
	#form_class = UploadForm
	template_name = 'schedule/schedule_import.html'
	#success_url = reverse_lazy('computer:computer_listar')

def scheduleCargarExcel(request):
	if request.method == 'POST':
		nombre_archivo = request.FILES.get('archivo')
		doc = openpyxl.load_workbook(nombre_archivo)
		nombres = doc.get_sheet_names()
		hoja = doc.get_sheet_by_name(nombres[0])
		datos = []
		lista = []
		for filas in hoja.rows:
			for columna in filas:
				if columna.value is not None:
					datos.append(columna.value)
			if len(datos)!=0:
					print datos
					lista.append(datos)
			datos = []

		ruta = handle_uploaded_file(nombre_archivo)
		context = {'lista':lista, 'nombre_archivo': nombre_archivo, 'ruta':ruta}
		return render(request, 'schedule/schedule_list_excel.html', context)


def scheduleCargarBase(request):
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
		
		numLab = Lab.objects.all().count()
		numDistributivo = Distributive.objects.all().count()
		lista_id = []
		if numLab != 0:
			if numDistributivo !=0:
				x = 0
				for fila in lista:
					if x == 0:
						x = x + 1
					else:
						laboratorio = Lab.objects.get(name_lab = str(fila[4])).id
						#distributivo = Distributive.objects.get(stage_dist = str(fila[3])).id_dist
						Schedule.objects.create(day=fila[0], hour_start=fila[1], hour_end=fila[2], dist_id=fila[3], lab_id=laboratorio)
				return HttpResponseRedirect(reverse('schedule:schedule_listar'))
			else:
				return HttpResponse("Primero debe cargar los registros de Distributive")
		else:
			return HttpResponse("Primero debe cargar los registros de laboratorio")


def handle_uploaded_file(f):
    with open('media/' + str(f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return str(f.name)