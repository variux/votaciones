# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth import authenticate, logout, login
from .forms import *
from .models import *

# Create your views here.


def index(request):
	ctx = {}
	return render(request, 'index.html', ctx)

def cedula(request):
	ctx = {}
	return render(request, 'cedula.html', ctx)
@csrf_exempt
def voto(request):
	id = request.POST.get('cedula')
	try:
		estudiante = Estudiante.objects.get(cedula = id)
		mesa = Mesa.objects.filter(is_available = False)
		data = {}
		data['nombre'] = estudiante.nombre
		data['mesa'] = mesa[0].id
	except ObjectDoesNotExist:
		data = {}
		data['nombre'] = 'No existe o Ya voto'
		data['mesa'] = '-1'
	return JsonResponse(data)


@csrf_exempt
def activate_table(request):

	try:
		check_student = Estudiante.objects.get(cedula = int(request.POST.get('student')))
		if check_student.do_vote == True:

			data = {}
			data['is_available'] = False
			data['mesa'] = -1
		else:
			try:

				table = request.POST.get('mesa')
				student = request.POST.get('student')
				estudiante = Estudiante.objects.get(cedula=int(student))
				estudiante.do_vote = True
				estudiante.save()
				mesa = Mesa.objects.get(id=table)
				mesa.is_available = True
				mesa.save()
				data = {}
				data['is_available'] = mesa.is_available
				data['mesa'] = mesa.id
			except ObjectDoesNotExist:

				data = {}
				data['is_available'] = False
				data['mesa'] = -1
	except ObjectDoesNotExist:

		data = {}
		data['is_available'] = False
		data['mesa'] = -1

	return JsonResponse(data)

def mesa(request, id_mesa):

	try:
		table = Mesa.objects.get(id=id_mesa)
		if(table.is_available == True):
			partidos = Partido.objects.all()
			ctx = {
				'nombre': table.titulo,
				'id_mesa': table.id,
				'partidos': partidos,
			}
			return render(request, 'mesa.html', ctx)
		else:
			ctx = {
				'id' : table.id,
			}

			return render(request, 'waiting.html', ctx)


		
	except ObjectDoesNotExist:
		return redirect('/votaciones/cedula/')

def check_table(request, id_mesa):
	table = int(id_mesa)
	try:
		mesa = Mesa.objects.get(id=table)
		if mesa.is_available == True:
			data = {
				'refresh': True,

			}
		else:
			data = {
				'refresh': False,
			}

		return JsonResponse(data)
	except ObjectDoesNotExist:
		data = {
			'refresh': False,
		}
		return JsonResponse(data)

def make_vote(request, mesa, partido):
	try:
		table = Mesa.objects.get(id=mesa)
		table.is_available = False
		table.save()

		party = Partido.objects.get(id=partido)
		if party.cantidad_votos == None:
			party.cantidad_votos = 1
		else:
			party.cantidad_votos = party.cantidad_votos + 1
		party.save()
		data = {
			'success': True
		}
		return JsonResponse(data)
	except ObjectDoesNotExist:
		data = {
			'success': False
		}
		return JsonResponse(data)



########################
# admin urls ###########
########################

def porcentaje(x, y):

	return 100*x/y
@login_required
def backend_index(request):
	votos_femeninos = Estudiante.objects.filter(gender=0, do_vote = True).count()
	votos_masculinos = Estudiante.objects.filter(gender=1, do_vote = True).count()
	total_votos = Partido.objects.aggregate(Sum('cantidad_votos'))
	abstencionismo_femenino = Estudiante.objects.filter(gender=0, do_vote = False).count()
	abstencionismo_masculino = Estudiante.objects.filter(gender = 1, do_vote = False).count()
	total_estudiantes = Estudiante.objects.all().count()
	per_abs_masculino = porcentaje(abstencionismo_masculino, total_estudiantes)
	per_abs_femenino = porcentaje(abstencionismo_femenino, total_estudiantes)
	per_femenino = porcentaje(votos_femeninos, total_estudiantes)
	per_masculino = porcentaje(votos_masculinos, total_estudiantes)
	faltante = total_votos['cantidad_votos__sum'] - (votos_femeninos + votos_masculinos)
	ctx = {
		'votos_femeninos': votos_femeninos,
		'votos_masculinos': votos_masculinos,
		'total_votos': total_votos['cantidad_votos__sum'],
		'abstencionismo_masculino': abstencionismo_masculino,
		'abstencionismo_femenino': abstencionismo_femenino,
		'per_abs_masculino': per_abs_masculino,
		'per_abs_femenino': per_abs_femenino,
		'per_masculino': per_masculino,
		'per_femenino': per_femenino,
		'faltante': faltante,

	}
	return render(request, 'backend/index.html', ctx)

def get_stats(request):
	votos_femeninos = Estudiante.objects.filter(gender=0, do_vote = True).count()
	votos_masculinos = Estudiante.objects.filter(gender=1, do_vote = True).count()
	total_votos = Partido.objects.aggregate(Sum('cantidad_votos'))
	abstencionismo_femenino = Estudiante.objects.filter(gender=0, do_vote = False).count()
	abstencionismo_masculino = Estudiante.objects.filter(gender = 1, do_vote = False).count()
	total_estudiantes = Estudiante.objects.all().count()
	per_abs_masculino = porcentaje(abstencionismo_masculino, total_estudiantes)
	per_abs_femenino = porcentaje(abstencionismo_femenino, total_estudiantes)
	per_femenino = porcentaje(votos_femeninos, total_estudiantes)
	per_masculino = porcentaje(votos_masculinos, total_estudiantes)
	faltante = total_votos['cantidad_votos__sum'] - (votos_femeninos + votos_masculinos)

	data = {
		'votos_femeninos': votos_femeninos,
		'votos_masculinos': votos_masculinos,
		'total_votos': total_votos['cantidad_votos__sum'],
		'abstencionismo_masculino': abstencionismo_masculino,
		'abstencionismo_femenino': abstencionismo_femenino,
		'per_abs_masculino': per_abs_masculino,
		'per_abs_femenino': per_abs_femenino,
		'per_masculino': per_masculino,
		'per_femenino': per_femenino,
		'faltante': faltante,
	}

	return JsonResponse(data)
@login_required
def view_partidos(request):
	partidos = Partido.objects.all().order_by('id')

	ctx = {
		'partidos' : partidos,
	}

	return render(request, 'backend/partido.html', ctx)
@login_required
def view_estudiantes(request):
	estudiantes = Estudiante.objects.all().order_by('id')
	ctx = {
		'estudiantes': estudiantes,
	}
	return render(request, 'backend/estudiante.html', ctx)
@login_required
def delete_estudiante(request, id_estudiante):
	estudiante = Estudiante.objects.get(id=id_estudiante)
	estudiante.delete()
	ctx = {
		'nombre_estudiante': estudiante.nombre,

	}
	return render(request, 'backend/eliminado_estudiante.html', ctx)
@login_required
def delete_partido(request, id_partido):
	partido = Partido.objects.get(id=id_partido)
	partido.delete()
	ctx = {
		'nombre_partido': partido.nombre,
	}
	return render(request, 'backend/eliminado.html', ctx)
@login_required
def edit_partido(request, id_partido):
	if request.method == 'GET':
		
		partido = Partido.objects.get(id=id_partido)
		ctx = {
			'partido': partido,
		}
		return render(request, 'backend/edit_partido.html', ctx)
	elif request.method == 'POST':
		id_partido = request.POST.get('id_partido')
		nombre = request.POST.get('nombre')
		bandera = request.FILES.get('bandera')
		slogan = request.POST.get('slogan')
		if 'bandera' in request.FILES:

			partido = Partido.objects.get(id=id_partido)
			partido.nombre = nombre
			partido.bandera = bandera
			partido.slogan = slogan
			partido.save()
		else:
			partido = Partido.objects.get(id=id_partido)
			partido.nombre = nombre
			partido.slogan = slogan
			partido.save()

		ctx = {
			'nombre_partido': nombre,
			'accion': 'editado',
		}
		return render(request, 'backend/success.html', ctx)
@login_required
def edit_estudiante(request, id_estudiante):
	if request.method == 'GET':
		
		estudiante = Estudiante.objects.get(id=id_estudiante)
		ctx = {
			'estudiante': estudiante,
		}
		return render(request, 'backend/edit_estudiante.html', ctx)
	elif request.method == 'POST':
		id_estudiante = request.POST.get('id_estudiante')
		nombre = request.POST.get('nombre')
		cedula = request.POST.get('cedula')
		if request.POST.get('do_vote') == '':
			do_vote = request.POST.get('do_vote')
		else:
			do_vote = False
		gender = request.POST.get('gender')
		estudiante = Estudiante.objects.get(id=id_estudiante)
		estudiante.nombre = nombre
		estudiante.cedula = cedula
		estudiante.do_vote = do_vote
		estudiante.gender = gender
		estudiante.save()

		ctx = {
			'nombre_estudiante': nombre,
			'accion': 'editado',
		}
		return render(request, 'backend/success_estudiante.html', ctx)
@login_required
def create_partido(request):
	if request.method == 'GET':
		create_partido = CreatePartido()
		ctx = {
			'create_partido': create_partido,
		}
		return render(request, 'backend/create_partido.html', ctx)
	elif request.method == 'POST':
		create_partido = CreatePartido(request.POST, request.FILES)
		if create_partido.is_valid():
			partido = Partido(None, create_partido.cleaned_data['nombre'], create_partido.cleaned_data['bandera'], create_partido.cleaned_data['slogan'], 0)
			partido.save()
			ctx = {
				'nombre_partido': create_partido.cleaned_data['nombre'],
				'accion': 'creado',
			}
			return render(request, 'backend/success.html', ctx)
		else:
			ctx = {
				'accion': 'creando'
			}
			return render(request, 'backend/error.html', ctx)
@login_required
def create_estudiante(request):
	if request.method == 'GET':
		create_estudiante = CreateEstudiante()
		ctx = {
			'create_estudiante': create_estudiante,
		}
		return render(request, 'backend/create_estudiante.html', ctx)
	elif request.method == 'POST':
		create_estudiante = CreateEstudiante(request.POST, request.FILES)
		if create_estudiante.is_valid():
			estudiante = Estudiante(None, create_estudiante.cleaned_data['nombre'], create_estudiante.cleaned_data['cedula'], create_estudiante.cleaned_data['do_vote'], create_estudiante.cleaned_data['gender'])
			estudiante.save()
			ctx = {
				'nombre_estudiante': create_estudiante.cleaned_data['nombre'],
				'accion': 'creado',
			}
			return render(request, 'backend/success_estudiante.html', ctx)
		else:
			ctx = {
				'accion': 'creando'
			}
			return render(request, 'backend/error.html', ctx)
@csrf_exempt
def login_user(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			auth = authenticate(username = username, password = password)

			if auth is not None:
				if auth.is_active:
					login(request, auth)
					data = {
						'logged': True,
						'message': 'Ingreso exitoso'

					}
					return JsonResponse(data)
				else:
					data = {
						'logged': False,
						'message': 'Usuario no activo'
					}
					return JsonResponse(data)
			else:
				data = {
					'logged': False,
					'message': 'El usuario o contraseña no son correctos'
				}
				return JsonResponse(data)
		elif request.method == "GET":
			ctx = {}
			return render(request, 'backend/login.html', ctx)
	else:
		return redirect('/votaciones/backend/')
def logout_user(request):
	logout(request)
	return redirect('/votaciones/backend/login/')

def get_active_tables(request):
	mesas = Mesa.objects.filter(is_available = True)
	mesas_ids_json = []
	mesas_names_json = []
	for mesa in mesas:
		mesas_ids_json.append(mesa.id)
		mesas_names_json.append(mesa.titulo)

	if not mesas:
		data = {
			'tables': [],
		}
	else:
		data = {
			'tables_ids': mesas_ids_json,
			'tables_names': mesas_names_json,
		}
	return JsonResponse(data)


					




	
					
