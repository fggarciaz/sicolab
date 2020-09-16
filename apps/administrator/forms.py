# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.administrator.models import Administrator
from datetime import datetime

#Formulario para Teachers
STATUS_CHOICE = (
		('1','Activo'),
		('0','Inactivo'),
	)

class AdministratorForm(forms.ModelForm):
	
	class Meta:
		model = Administrator

		fields = [
			'dni_adm',
			'names_adm',
			'email_adm',
			'password_adm',
			'status',
		]

		labels = {
			'dni_adm': 'Cédula',
			'names_adm': 'Administrador',
			'email_adm': 'E-mail',
			'password_adm': 'Contraseña',
			'status': 'Estado',	
		}

		widgets = {
			'dni_adm':forms.TextInput(attrs = {'class': 'form-control'} ),
			'names_adm':forms.TextInput(attrs = {'class': 'form-control'} ),
			'email_adm':forms.TextInput(attrs = {'class': 'form-control'} ),
			'password_adm':forms.TextInput(attrs = {'class': 'form-control'} ),
			'status':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
		}


#Formulario para Subjects
ahora = datetime.now()
stage1 = str(ahora.year)+'-1'
stage2 = str(ahora.year)+'-2'
STAGE_CHOICE = (
	(stage1,stage1),
	(stage2,stage2),
	)
