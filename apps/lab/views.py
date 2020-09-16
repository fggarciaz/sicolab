# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework import generics

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.lab.forms import LabForm, ComputerForm
from apps.lab.models import Lab, Computer
from apps.lab.serializers import LabSerializer, ComputerSerializer

from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

# Create your views here.
#------ Vistas para Labs

def index(request):
	#return HttpResponse("Hola")
	return render(request, 'lab/index.html')

class LabList(ListView):
	#model = Lab
	queryset = Lab.objects.order_by('id_lab')
	template_name = 'lab/lab_list.html'

class LabCreate(CreateView):
	model = Lab
	form_class = LabForm
	template_name = 'lab/lab_form.html'
	success_url = reverse_lazy('lab:lab_listar')

class LabUpdate(UpdateView):
	model = Lab
	form_class = LabForm
	template_name = 'lab/lab_form.html'
	success_url = reverse_lazy('lab:lab_listar')

class LabDelete(DeleteView):
	model = Lab
	template_name = 'lab/lab_delete.html'
	success_url = reverse_lazy('lab:lab_listar')


class LabAPI_List(generics.ListCreateAPIView):
	queryset = Lab.objects.all()
	serializer_class = LabSerializer
	#filter_backends = (filters.DjangoFilterBackend,)
	#filter_field = ('id_lab')
	
class LabAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Lab.objects.all()
	serializer_class = LabSerializer
	#filter_backends = (filters.DjangoFilterBackend,)
	#filter_field = ('id_lab')

def LabReport(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="Reporte_Labs.pdf"'
	#response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	c.setTitle('Reporte de Laboratorios')

	#Header
	c.setLineWidth(.3)
	c.setFont('Helvetica', 22)
	c.drawString(4*cm, 27*cm,'SICOLAB')
	c.setFont('Helvetica', 14)
	c.drawString(4*cm, 26*cm,'Reporte de Laboratorios')
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
	labo = Paragraph('<b>Laboratorio</b>', styleBH)	

	data = []
	data.append([num, labo])

	#Table
	styleN = styles['BodyText']
	styleN.alignment = TA_CENTER
	styleN.fontSize = 7
	high = 650
	
	for lab in Lab.objects.all():
		row = [lab['id_lab'], lab['name_lab']]
		data.append(row)
		high = high - 18
	
	#Table size
	width, height = A4
	table = Table(data, colWidths=[2*cm, 17*cm])
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


#------ Vistas para Computers

class ComputerList(ListView):
	#model = Computer
	queryset = Computer.objects.order_by('name_comp')
	template_name = 'lab/computer_list.html'

class ComputerCreate(CreateView):
	model = Computer
	form_class = ComputerForm
	template_name = 'lab/computer_form.html'
	success_url = reverse_lazy('computer:computer_listar')

class ComputerUpdate(UpdateView):
	model = Computer
	form_class = ComputerForm
	template_name = 'lab/computer_form.html'
	success_url = reverse_lazy('computer:computer_listar')

class ComputerDelete(DeleteView):
	model = Computer
	template_name = 'lab/computer_delete.html'
	success_url = reverse_lazy('computer:computer_listar')

class ComputerAPI_List(generics.ListCreateAPIView):
	queryset = Computer.objects.all()
	serializer_class = ComputerSerializer

class ComputerAPI_Detail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Computer.objects.all()
	serializer_class = ComputerSerializer
	lookup_field = 'mac_comp'

class ComputerAPI_Detail2(generics.RetrieveAPIView):
	lookup_field = 'mac_comp'
	serializer_class = ComputerSerializer

	def get_queryset(self):
		mac_comp2 = self.kwargs['mac_comp']
		print mac_comp2
		comp = None
		try:
			comp = Computer.objects.get(mac_comp=mac_comp2)
			if comp is not None:
				print "si existe"
				return Computer.objects.all()
		except Computer.DoesNotExist: 
			lab = Lab.objects.get(id_lab=self.request.GET.get('lab', None))
			comp = Computer(name_comp=self.request.GET.get('name_comp', None),mac_comp=mac_comp2,ip_comp=self.request.GET.get('ip_comp', ''), lab=lab)
			comp.save();
			print "No Existe 2"
			return Computer.objects.all()
		return comp

def ComputerReport(request):

	if request.method == 'POST':
		lab_opc = request.POST['selectLaboratorio'];
		


		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'filename="Reporte_Computadores.pdf"'

		styles = getSampleStyleSheet()

		styleN = styles["BodyText"]
		styleN.alignment = TA_LEFT
		styleN.fontSize = 6.2

		styleBH = styles["Normal"]
		styleBH.alignment = TA_CENTER
		styleBH.fontSize = 10
		styleBH.color = colors.white


		img= (Image('static/images/sicolab_carr.png', width=17*cm, height=3.2*cm))	
	   
		pc= Paragraph("\nCOMPUTADOR\n", styleBH)
		mac= Paragraph("\nMAC\n", styleBH)
		ip= Paragraph("\nDDIRECCIÓN IP\n", styleBH)
		

		estilos_tabla=[                    
			('GRID', (0, 1), (-1, -1), 0.5, colors.transparent),
			('BOX', (0, 0), (-1, -1), 2, colors.gray),
			('BACKGROUND', (0, 0), (12, 0), colors.lightblue),
			('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
			('FONTSIZE', (0, 0), (-1, 0), 12),
	 
			]

		p = canvas.Canvas(response,  pagesize=A4)


		if lab_opc == "Todos":

			for lab in Lab.objects.all():

				img.drawOn(p , 2*cm, 25*cm)
				p.setFont('Helvetica', 13)
				p.drawString(2*cm, 24*cm, lab.name_lab)
				width, height = A4	
				height_t=650
				datos = [[pc, mac, ip]]

				

				for comp in Computer.objects.all():

					row= []

					if lab.id_lab == comp.lab_id:
						row=[comp.name_comp, comp.mac_comp, comp.ip_comp]
						height_t=height_t-16

						print row
						datos.append(row)

				tabla = Table(data=datos,  style= estilos_tabla  , colWidths=[135, 135],
							rowHeights=15)
				tabla.Align = "CENTER"
				tabla.wrapOn(p, width, height)
				tabla.drawOn(p,  3.6*cm, height_t-2)
				p.setFont('Helvetica', 11)
				p.drawString(3*cm, 3*cm, "___________________________")
				p.drawString(4*cm, 2.3*cm, "Administrador de TIC")
				#p.drawString(2.5*cm, 1.8*cm, "Ing. Ronald Christopher Elizalde López")
				p.drawString(13*cm, 3*cm, "__________________________")
				p.drawString(13.6*cm, 2.3*cm, "Coordinador de la carrera")
				#p.drawString(13.01*cm, 1.8*cm, "Ing. Jimmy Rolando Molina Rios")
				p.showPage()
		

		if lab_opc != "Todos":

			print "hola prro"

			for lab in Lab.objects.filter(id_lab=lab_opc):


				img.drawOn(p , 2*cm, 25*cm)
				p.setFont('Helvetica', 13)
				p.drawString(2*cm, 24*cm, lab.name_lab)
				width, height = A4	
				height_t=650
				datos = [[pc, mac, ip]]

				for comp in Computer.objects.all():

					row= []

					if lab.id_lab == comp.lab_id:
						row=[comp.name_comp, comp.mac_comp, comp.ip_comp]
						height_t=height_t-16
						print row
						datos.append(row)
				
				tabla = Table(data=datos,  style= estilos_tabla  , colWidths=[135, 135],
							rowHeights=15)
				tabla.Align = "CENTER"
				tabla.wrapOn(p, width, height)
				tabla.drawOn(p,  3.6*cm, height_t-2)
				p.setFont('Helvetica', 11)
				p.drawString(3*cm, 3*cm, "___________________________")
				p.drawString(4*cm, 2.3*cm, "Administrador de TIC")
				#p.drawString(2.5*cm, 1.8*cm, "Ing. Ronald Christopher Elizalde López")
				p.drawString(13*cm, 3*cm, "__________________________")
				p.drawString(13.6*cm, 2.3*cm, "Coordinador de la carrera")
				#p.drawString(13.01*cm, 1.8*cm, "Ing. Jimmy Rolando Molina Rios")
				
			p.showPage()
		
		p.save()

		return response

