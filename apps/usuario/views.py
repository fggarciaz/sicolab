# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

#from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import UsuarioForm, UsuarioUpdateForm

# Create your views here.

class UsuarioCreate(CreateView):
	model = User
	template_name = "usuario/usuario_registro.html"
	form_class = UsuarioForm
	success_url = reverse_lazy('home:index')

class UsuarioList(ListView):
	#model = Lab
	queryset = User.objects.order_by('id')
	template_name = 'usuario/usuario_listar.html'

class UsuarioUpdate(UpdateView):
	model = User
	template_name = 'usuario/usuario_update.html'
	form_class = UsuarioUpdateForm
	success_url = reverse_lazy('usuario:listar')

class UsuarioDelete(DeleteView):
	model = User
	template_name = 'usuario/usuario_delete.html'
	success_url = reverse_lazy('usuario:listar')