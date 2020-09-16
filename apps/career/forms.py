# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms

from apps.career.models import Career, Semester

# ----- Clase CareerForm

CAREER_CHOICE = (
		('Matutino','Matutino'),
		('Vespertino','Vespertino'),
		('Nocturno','Nocturno'),
	)

class CareerForm(forms.ModelForm):

	class Meta:
		model = Career

		fields = [
			'name_car',
			'section_car',
		]

		labels = {
			'name_car': 'Carrera',
			'section_car': 'Sección',
		}

		widgets = {
			'name_car': forms.TextInput(attrs = {'class': 'form-control'} ),
			'section_car': forms.Select(choices = CAREER_CHOICE, attrs = {'class': 'form-control'} ),
		}

# ----- Clase CareerForm

SEMESTER_CHOICE = (
		('Primero','Primero'), ('Segundo','Segundo'),
		('Tercero','Tercero'), ('Cuarto','Cuarto'),
		('Quinto','Quinto'), ('Sexto','Sexto'),
		('Séptimo','Séptimo'), ('Octavo','Octavo'),
		('Noveno','Noveno'), ('Décimo','Décimo'),
	)

PARALLEL_CHOICE = (
		('A','A'),
		('B','B'),
		('C','C'),
		('D','D'),
	)

YEAR_CHOICE = (
		(2017,2017), (2018,2018), (2019,2019), (2020,2020), (2021,2021),
		(2022,2022), (2023,2023), (2024,2024), (2025,2025), (2026,2026),
	)

class SemesterForm(forms.ModelForm):

	class Meta:
		model = Semester

		fields = [
			'name_sem',
			'parallel_sem',
			#'year_sem',
			'car',
		]

		labels = {
			'name_sem': 'Semestre',
			'parallel_sem': 'Paralelo',
			#'year_sem': 'Año',
			'car': 'Carrera',
		}

		widgets = {
			'name_sem': forms.Select(choices = SEMESTER_CHOICE, attrs = {'class': 'form-control'} ),
			'parallel_sem': forms.Select(choices = PARALLEL_CHOICE, attrs = {'class': 'form-control'} ),
			#'year_sem': forms.Select(choices = YEAR_CHOICE, attrs = {'class': 'form-control'} ),
			'car': forms.Select(attrs = {'class': 'form-control'} ),
		}