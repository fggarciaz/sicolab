# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.schedule.models import Schedule




SEMESTER_CHOICE = (
		('Primero','Primero'), ('Segundo','Segundo'),
		('Tercero','Tercero'), ('Cuarto','Cuarto'),
		('Quinto','Quinto'), ('Sexto','Sexto'),
		('Séptimo','Séptimo'), ('Octavo','Octavo'),
		('Noveno','Noveno'), ('Décimo','Décimo'),
	)

DAY_CHOICE = (
		('1','Lunes'),
		('2','Martes'),
		('3','Miércoles'),
		('4','Jueves'),
		('5','Viernes'),

	)


class ScheduleForm(forms.ModelForm):

	class Meta:
		model = Schedule

		fields = [
			#'stage',
			'day',
			'hour_start',
			'hour_end',
			'lab',
			#'sub',
			'dist',
		]

		labels = {
			#'stage':'Etapa',
			'day':'Día',
			'hour_start':'Hora Inicio',
			'hour_end':'Hora Fin',
			'lab':'Laboratorio',
			#'sub':'Asignatura',
			'dist':'Distributive',
			
		}

		widgets = {
			#'stage': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Escriba la etapa ejemplo: 2018-1', 'autocomplete' : 'off', 'required':'required'} ),
			'day': forms.Select(choices = DAY_CHOICE, attrs = {'class': 'form-control'} ),
			'hour_start': forms.TimeInput(attrs = {'class': 'form-control timepicker', 'type': 'time', 'required':'required'} ),
			'hour_end': forms.TimeInput(attrs = {'class': 'form-control timepicker', 'type': 'time', 'required':'required'} ),
			#'year_sem': forms.Select(choices = YEAR_CHOICE, attrs = {'class': 'form-control'} ),
			'lab': forms.Select(attrs = {'class': 'form-control', 'required':'required'} ),
			#'sub': forms.Select(attrs = {'class': 'form-control', 'required':'required'} ),
			'dist': forms.Select(attrs = {'class': 'form-control', 'required':'required'} ),
		}