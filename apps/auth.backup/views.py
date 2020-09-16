# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from apps.student import serializers as StudentSerializer
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

import md5
from apps.student.models import Student
from apps.schedule.models import Schedule
from apps.teacher.models import Teacher
from apps.distributive.models import Stage, Distributive
from apps.guest.models import Guest
#from apps.schedule.models import Schedule

from apps.guest.serializers import GuestSerializer
from apps.schedule.serializers import ScheduleSerializer
from apps.student.serializers import StudentSerializer
from apps.teacher.serializers import TeacherSerializer
from apps.distributive.serializers import DistributiveSerializer, DistributiveSerializerApi

# Create your views here.
@api_view(['POST'])
def studentLogin(request):
    if request.method == 'POST':
    	content = {'detail': 'Error complete el Formulario'}
    	dni = request.POST.get("dni_stu")
    	password = request.POST.get("password_stu")
        print "ssssssssssssssssss"
        if dni is not None and password is not None:
        	try:
        		student = Student.objects.get(dni_stu=dni, password_stu=md5.new(password).hexdigest(),status_stu=1)
        		serializers = StudentSerializer(student)
        		return Response(serializers.data, status=status.HTTP_200_OK)
        	except Student.DoesNotExist:
        		try:
	        		teacher = Teacher.objects.get(dni_tea=dni, password_tea=md5.new(password).hexdigest(),status=1)
	        		serializers = TeacherSerializer(teacher)
	        		return Response(serializers.data, status=status.HTTP_200_OK)
	        	except Teacher.DoesNotExist:
	        		content = {'detail': 'Usuario o Contraseña Incorrectos!'}
	        		return Response(content, status=status.HTTP_400_BAD_REQUEST)
        	return Response(content, status=status.HTTP_200_OK)
    	return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def externalLogin(request):
    if request.method == 'POST':
        content = {'detail': 'Error complete el Formulario'}
        password = request.POST.get("password_stu")
        if password is not None:
            try:
                guest = Guest.objects.get(password_access=md5.new(password).hexdigest(),status=1)
                serializers = GuestSerializer(guest)
                return Response(serializers.data, status=status.HTTP_200_OK)
            except Guest.DoesNotExist:
                    content = {'detail': 'Clave de Acceso Incorrecta!'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
            return Response(content, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getDistributive(request):
    if request.method == 'GET':
        content = {'detail': 'Error complete el Formulario [lab_id, dni_stu, h_current, day]'}
        lab_id = request.GET.get("lab_id")
        dni = request.GET.get("dni")
        stage_ = request.GET.get("stage")
        h_current = "08:00:00" 
        #debemos obterner hora actual del servidor
        day = request.GET.get("day")
        if stage_ is not None and lab_id is not None and h_current is not None and day is not None and dni is not None:
            try:
                stage = Stage.objects.get(name_sta=stage_)
                sched = Schedule.objects.get(lab_id=lab_id, hour_start__lte=h_current,hour_end__gte=h_current, day=day)
                student = Student.objects.get(dni_stu=dni, status_stu=1)
                distributive_ = student.dist.get(id_dist=sched.dist.id_dist)
                if(distributive_ is not None and str(distributive_.sta) == stage_):
                    content = {
                        'id_dist': distributive_.id_dist,
                        'hour_end': sched.hour_end,
                        'hour_start': sched.hour_start,
                        'hour_current': h_current,
                        'sta': ''+str(distributive_.sta),
                        'sem': ''+str(distributive_.sem),
                        'tea': ''+str(distributive_.tea),
                        'sub': ''+str(distributive_.sub)
                        }
                    return Response(content, status=status.HTTP_200_OK)
                else:
                    content = {'detail': 'Error, Esta cedula no pertenece a ninguna materia en este Laboratorio a esta Hora '+str(distributive_.sta)}                
                '''select * from schedule_schedule join student_student_dist on schedule_schedule."day" = '1' and 
                schedule_schedule.lab_id =1 and schedule_schedule.hour_end > '07:00:00' and 
                schedule_schedule.dist_id = student_student_dist.distributive_id  and student_id =1'''
            except Stage.DoesNotExist as e:
                    content = {'detail': 'Error, No Existe El periodo Académico Indicado'} 
            except Schedule.DoesNotExist as e:
                    content = {'detail': 'Error, No Existe Materias a esta hora en este Laboratorio'}
            except Student.DoesNotExist as e:
                    content = {'detail': 'Error, Esta cedula no consta en esta materia en este Laboratorio a esta Hora'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)