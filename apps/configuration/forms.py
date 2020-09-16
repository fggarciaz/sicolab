# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.configuration.models import Configuration
from datetime import datetime


ahora = datetime.now()
stage1 = str(ahora.year)+'-1'
stage2 = str(ahora.year)+'-2'
STAGE_CHOICE = (
	(stage1,stage1),
	(stage2,stage2),
	)

STATUS_CHOICE = (
		('1','Activo'),
		('0','Inactivo'),
	)


class ConfigurationForm(forms.ModelForm):
	
	class Meta:
		model = Configuration

		fields = [
			'stage_config',
			'lock_all',
		]

		labels = {
			'stage_config': 'Periodo',
			'lock_all': 'lock',
		}

		widgets = {

			'stage_config':forms.Select(choices = STAGE_CHOICE, attrs = {'class': 'form-control'} ),
			'lock_all':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
		}
