# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.guest.models import Guest

# ----- Clase UsuarioForm
STATUS_CHOICE = (
		('1','Activo'),
		('0','Inactivo'),
	)

class GuestForm(forms.ModelForm):
	
	class Meta:
		model = Guest

		fields = [
			'id_guest',
			'description',
			'password_access',
			'start_time',
			'finish_time',
			'status',
			'lab',
		]

		labels = {
			'id_guest': 'N°',
			'description': 'Descripción',
			'password_access': 'Contraseña',
			'start_time': 'Hora Inicio',
			'finish_time': 'Hora Fin',
			'status': 'Estado',
			'lab': 'Laboratorio',
		}

		widgets = {
			'id_guest':forms.TextInput(attrs = {'class': 'form-control'} ),
			'description':forms.TextInput(attrs = {'class': 'form-control'} ),
			'password_access':forms.TextInput(attrs = {'class': 'form-control'} ),
			'start_time': forms.DateTimeInput(attrs = {'class': 'form-control', 'type': 'time', 'required':'required'} ),
			'finish_time': forms.DateTimeInput(attrs = {'class': 'form-control', 'type': 'time', 'required':'required'} ),
			'status':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
			'lab': forms.Select(attrs = {'class': 'form-control', 'required':'required'} ),
		}