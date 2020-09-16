from __future__ import absolute_import, unicode_literals
from django import forms

from apps.lab.models import Lab, Computer

class LabForm(forms.ModelForm):
	
	class Meta:
		model = Lab

		fields = [
			'name_lab',
			#'ip1_lab',
			#'ip2_lab',
		]

		labels = {
			'name_lab': 'Laboratorio',
			#'ip1_lab': 'IP Inicio',
			#'ip2_lab': 'IP FIn',
		}

		widgets = {
			'name_lab':forms.TextInput(attrs = {'class': 'form-control'} ),
			#'ip1_lab':forms.TextInput(attrs = {'class': 'form-control'} ),
			#'ip2_lab':forms.TextInput(attrs = {'class': 'form-control'} ),
		}

class ComputerForm(forms.ModelForm):

	class Meta:
		model = Computer

		fields = [
			'name_comp',
			'mac_comp',
			'ip_comp',
			'lab',
		]

		labels = {
			'name_comp': 'Computadora',
			'mac_comp': 'MAC',
			'ip_comp': 'IP',
			'lab': 'Laboratorio',
		}

		widgets = {
			'name_comp':forms.TextInput(attrs = {'class': 'form-control'} ),
			'mac_comp':forms.TextInput(attrs = {'class': 'form-control'} ),
			'ip_comp':forms.TextInput(attrs = {'class': 'form-control'} ),
			'lab':forms.Select(attrs = {'class': 'form-control'} ),
		}