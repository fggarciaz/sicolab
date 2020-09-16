# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from apps.student import serializers as StudentSerializer
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

import time

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
        lab = request.POST.get("lab_id")
        h_current = time.strftime("%Y-%m-%d %H:%M:%S")
        if password is not None and lab is not None:
            try:
                guest = Guest.objects.get(password_access=md5.new(password).hexdigest(),lab_id=lab,start_time__lte=h_current,finish_time__gte=h_current,status=1)
                #serializers = GuestSerializer(guest)
                content = {
                        'id_guest': guest.id_guest,
                        'description': guest.description,
                        'password_access': guest.password_access,
                        'hour_current': h_current,
                        'start_time': guest.start_time,
                        'finish_time': guest.finish_time,
                        'created_at': guest.created_at,
                        'updated_at': guest.updated_at,
                        'status': guest.status,
                        'lab': guest.lab.id_lab
                        }
                return Response(content, status=status.HTTP_200_OK)
                #return Response(serializers.data, status=status.HTTP_200_OK)

            except Guest.DoesNotExist:
                    content = {'detail': 'Acceso denegado o caducado para esta contraseña', 'hour_current': h_current,}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
            return Response(content, status=status.HTTP_200_OK)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getDistributive(request):
    if request.method == 'GET':
        n_day = {'MON':1,'TUE':2,'WEB':3,'THU':4,'FRI':5,'SAT':6,'SUN':7}
        content = {'detail': 'Error complete el Formulario [lab_id, dni]'}
        lab_id = request.GET.get("lab_id")
        dni = request.GET.get("dni")
        stage_ = str(time.strftime("%Y"))
        if int(time.strftime("%m"))>=10:
            stage_ += "-2"
        elif int(time.strftime("%m"))<=2:
            stage_ = str((int(time.strftime("%Y"))-1)) + "-2"
        elif int(time.strftime("%m")) >= 3:
            stage_ = time.strftime("%Y") + "-1" 
        h_current = time.strftime("%H:%M:%S") 
        day = n_day[time.strftime("%a").upper()]
        #debemos obterner hora actual del servidor
        print ""
        print (str(stage_) + "   " +str(h_current) + " ****************************** " + str(day) )
        print ""
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
                    content = {'detail': 'Acceso no disponible en este Laboratorio','hour_current': h_current}                
            except Stage.DoesNotExist as e:
                    content = {'detail': 'Periodo Académico sin registros', 'stage':stage_} 
            except Schedule.DoesNotExist as e:
                    content = {'detail': 'Horario Libre en este Laboratorio', 'stage':stage_}
            except Distributive.DoesNotExist as e:
                    content = {'detail': 'No existe matricula para esta cédula', 'stage':stage_}
            except Student.DoesNotExist as e:
                    try:
                        teacher = Teacher.objects.get(dni_tea=dni, status=1)
                        distributive_ = Distributive.objects.get(id_dist=sched.dist.id_dist, tea=teacher.id_tea)
                        if(distributive_ is not None):
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
                            content = {'detail': 'Acceso no disponible en este Laboratorio','hour_current': h_current}
                    except Teacher.DoesNotExist as e:
                            content = {'detail': 'Usuario Incorrecto', 'stage':stage_}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response(content, status=status.HTTP_400_BAD_REQUEST)