# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.distributive.models import Stage, Distributive
from datetime import datetime

ahora = datetime.now()
stage1 = str(ahora.year)+'-1'
stage2 = str(ahora.year)+'-2'
# STAGE_CHOICE = (
# 	(stage1, stage1),
# 	(stage2, stage2),
# 	)

class StageForm(forms.ModelForm):

	class Meta:
		model = Stage

		fields = [
			'name_sta',
			'start_date',
			'end_date'
		]

		labels = {
			'name_sta': 'Periodo',
			'start_date': 'Fecha Inicio',
			'end_date': 'Fecha Fin',		
		}

		widgets = {
			'name_sta':forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'2017-1'} ),
			'start_date':forms.DateInput(attrs = {'class': 'form-control timepicker', 'type': 'date'} ),
			'end_date':forms.DateTimeInput(attrs = {'class': 'form-control timepicker', 'type': 'date'} ),			
		}

class DistributiveForm(forms.ModelForm):
	
	class Meta:
		model = Distributive

		fields = [
			'sta',			
			'sem',
			'tea',
			'sub',
		]

		labels = {			
			'sta': 'Periodo',
			'sem': 'Semestre',
			'tea': 'Docente',
			'sub': 'Asignatura',
		}

		widgets = {
			'sta':forms.Select(attrs = {'class': 'form-control'} ),
			'sem':forms.Select(attrs = {'class': 'form-control'} ),
			'tea':forms.Select(attrs = {'class': 'form-control'} ),
			'sub':forms.Select(attrs = {'class': 'form-control'} ),
		}