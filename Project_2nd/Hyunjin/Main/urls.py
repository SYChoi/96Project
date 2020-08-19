from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('greeting/', views.greeting, name='greeting'),
	path('contact/', views.contact, name='contact'),
	path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
	path('notice/', views.notice, name='notice'),
#	path('notice_create/', views.notice_create, name='notice_create'),
	path('antirust/', views.antirust, name='antirust'),
	path('equip/', views.equip, name='equip'),
	path('consulting/', views.consulting, name='consulting'),
	path('online_consult/', views.online_consult, name='online_consult'),
	path('raw_material/', views.raw_mat, name='raw_mat'),
	path('industrial_part/', views.indust_part, name='indust_part'),
	path('download/', views.download, name='download'),
	path('engine_material/', views.engine_mat, name='engine_mat'),
	path('BA/', views.BA, name='BA'),
]
