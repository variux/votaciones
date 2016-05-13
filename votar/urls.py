from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
	url(r'^cedula/', views.cedula, name='cedula'),
	url(r'^get-vote/', views.voto, name='voto'),
	url(r'^activate-table/', views.activate_table, name='activate-table'),
	url(r'^mesa/(?P<id_mesa>[0-9]+)/', views.mesa, name='mesa'),
	url(r'^check-table/(?P<id_mesa>[0-9]+)/', views.check_table, name='check_table'),
	url(r'^make-vote/(?P<mesa>[0-9]+)/(?P<partido>[0-9]+)/', views.make_vote, name='make_vote'),
	url(r'^backend/$', views.backend_index, name='backend_index'),
	url(r'^get-stats/$', views.get_stats, name='get_stats'),
	url(r'^backend/ver-partidos/', views.view_partidos, name='view_partidos'),
	url(r'^backend/ver-estudiantes/', views.view_estudiantes,  name='view_estudiantes'),
	url(r'^backend/eliminar-partido/(?P<id_partido>[0-9]+)/', views.delete_partido, name='delete_partidos'),
	url(r'^backend/eliminar-estudiante/(?P<id_estudiante>[0-9]+)/', views.delete_estudiante, name='delete_estudiante'),
	url(r'^backend/editar-partido/(?P<id_partido>[0-9]+)/', views.edit_partido, name='edit_partido'),
	url(r'^backend/editar-estudiante/(?P<id_estudiante>[0-9]+)/', views.edit_estudiante, name='edit_estudiante'),
	url(r'^backend/crear-partido/', views.create_partido, name='create_partido'),
	url(r'^backend/crear-estudiante/', views.create_estudiante, name='create_estudiante'),
	url(r'^backend/login/', views.login_user, name='login'),
	url(r'^backend/logout/', views.logout_user, name='logout'),
	url(r'^backend/get-active-tables/', views.get_active_tables, name='get_active_tables'),






]