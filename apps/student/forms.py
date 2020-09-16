# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.student.models import Student

#Formulario para Students
STATUS_CHOICE = (
		('1','Activo'),
		('0','Inactivo'),
	)

class StudentForm(forms.ModelForm):
	
	class Meta:
		model = Student

		fields = [
			'dni_stu',
			'names_stu',
			'email_stu',
			'status_stu',
			#'sub',
			'dist',
		]

		labels = {
			'dni_stu': 'Cédula',
			'names_stu': 'Estudiante',
			'email_stu': 'E-mail',
			'status_stu': 'Estado',
			#'sub':'Asignatura',	
			'dist':'Distributivo',	
		}

		widgets = {
			'dni_stu':forms.TextInput(attrs = {'class': 'form-control', 'maxlength':'10'} ),
			'names_stu':forms.TextInput(attrs = {'class': 'form-control'} ),
			'email_stu':forms.TextInput(attrs = {'class': 'form-control'} ),
			'status_stu':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
			#'sub': forms.CheckboxSelectMultiple(),
			'dist': forms.CheckboxSelectMultiple(attrs = {'id':'listado'}),
		}

	def clean_dni_stu(self):
		msg1 = "La cédula debe ser de 10 dígitos"
		msg = "La cédula introducida no es válida"
		ced = self.cleaned_data['dni_stu']
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


class StudentUpdate(forms.ModelForm):
	class Meta:
		model = Student

		fields = [
			'dni_stu',
			'names_stu',
			'password_stu',
			'email_stu',
			'status_stu',
			#'sub',
			'dist',
		]

		labels = {
			'dni_stu': 'Cédula',
			'names_stu': 'Estudiante',
			'password_stu': 'Contraseña',
			'email_stu': 'E-mail',
			'status_stu': 'Estado',
			#'sub':'Asignatura',	
			'dist':'Distributivo',	
		}

		widgets = {
			'dni_stu':forms.TextInput(attrs = {'class': 'form-control', 'maxlength':'10','readonly':'true'} ),
			'names_stu':forms.TextInput(attrs = {'class': 'form-control'} ),
			'password_stu':forms.TextInput(attrs = {'class': 'form-control'} ),
			'email_stu':forms.TextInput(attrs = {'class': 'form-control'} ),
			'status_stu':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
			#'sub': forms.CheckboxSelectMultiple(),
			'dist': forms.CheckboxSelectMultiple(),
		}