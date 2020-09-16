from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms

STATUS_CHOICE = (
		('1','Activo'),
		('0','Inactivo'),
	)

class UsuarioForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
				'is_active':'Estado',
		}
		widgets = {
			'username':forms.TextInput(attrs = {'class': 'form-control', 'maxlength':'20'} ),
			'first_name':forms.TextInput(attrs = {'class': 'form-control'} ),
			'last_name':forms.TextInput(attrs = {'class': 'form-control'} ),
			'email':forms.TextInput(attrs = {'class': 'form-control'} ),
			'is_active':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
		}

class UsuarioUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'is_active'
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
				'is_active':'Estado',
		}
		widgets = {
			'username':forms.TextInput(attrs = {'class': 'form-control', 'maxlength':'20'} ),
			'first_name':forms.TextInput(attrs = {'class': 'form-control'} ),
			'last_name':forms.TextInput(attrs = {'class': 'form-control'} ),
			'email':forms.TextInput(attrs = {'class': 'form-control'} ),
			'is_active':forms.Select(choices = STATUS_CHOICE, attrs = {'class': 'form-control'} ),
			}