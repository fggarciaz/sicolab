# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.teacher.models import Teacher, Subject
from datetime import datetime

#Formulario para Teachers
STATUS_CHOICE = (
		('1','Activo'),
		('0','Inactivo'),
	)

class TeacherForm(forms.ModelForm):
	
	class Meta:
		model = Teacher

		fields = [
			'dni_tea',
			#'password_tea',
			'names_tea',
			'email_tea',
			'status',
		]

		labels = {
			'dni_tea': 'Cédula',
			#'password_tea': 'Contraseña',
			'names_tea': 'Docente',
			'email_tea': 'E-mail',
			'status': 'Estado',	
		}

		widgets = {
			'dni_tea':forms.TextInput(attrs = {'class': 'form-control'} ),
			#'password_tea':forms.TextInput(attrs = {'class': 'form-control'} ),
			'names_tea':forms.TextInput(attrs = {'class': 'form-control'} ),
			'email_tea':forms.TextInput(attrs = {'class': 'form-control'} ),
			'status':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
		}

	def clean_dni_tea(self):
		msg1 = "La cédula debe ser de 10 dígitos"
		msg = "La cédula introducida no es válida"
		ced = self.cleaned_data['dni_tea']
		print 'Hola entre al clean_dni_stu'
		if len(ced) == 10:
			valores = [ int(ced[x]) * (2 - x % 2) for x in range(9) ]
			suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
			veri = 10 - (suma - (10 * (suma / 10)))
			if int(ced[9]) == int (str(veri)[-1:]):
				return ced
			else:
				raise forms.ValidationError(msg)
		else:
			raise forms.ValidationError(msg1)

class TeacherUpdate(forms.ModelForm):
	
	class Meta:
		model = Teacher

		fields = [
			'dni_tea',
			#'password_tea',
			'names_tea',
			'email_tea',
			'status',
		]

		labels = {
			'dni_tea': 'Cédula',
			#'password_tea': 'Contraseña',
			'names_tea': 'Docente',
			'email_tea': 'E-mail',
			'status': 'Estado',	
		}

		widgets = {
			'dni_tea':forms.TextInput(attrs = {'class': 'form-control','readonly':'true'} ),
			#'password_tea':forms.TextInput(attrs = {'class': 'form-control'} ),
			'names_tea':forms.TextInput(attrs = {'class': 'form-control'} ),
			'email_tea':forms.TextInput(attrs = {'class': 'form-control'} ),
			'status':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
		}

#Formulario para Subjects
# ahora = datetime.now()
# stage1 = str(ahora.year)+'-1'
# stage2 = str(ahora.year)+'-2'
# STAGE_CHOICE = (
# 	(stage1,stage1),
# 	(stage2,stage2),
# 	)

class SubjectForm(forms.ModelForm):
	
	class Meta:
		model = Subject

		fields = [
			'name_sub',
			#'stage_sub',
			#'sem',
			#'tea',
		]

		labels = {
			'name_sub': 'Asignatura',
			#'stage_sub': 'Periodo',
			#'sem': 'Semestre',
			#'tea': 'Docente',
		}

		widgets = {
			'name_sub':forms.TextInput(attrs = {'class': 'form-control'} ),			
			#'stage_sub':forms.Select(choices = STAGE_CHOICE, attrs = {'class': 'form-control'} ),
			#'sem':forms.Select(attrs = {'class': 'form-control'} ),
			#'tea':forms.Select(attrs = {'class': 'form-control'} ),
		}