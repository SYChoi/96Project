from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
        path('greeting/', views.greeting),
	path('contact/', views.contact),
	path('notice/', views.notice),
	path('antirust/', views.antirust),
	path('equip/', views.equip),
	path('consulting/', views.consulting),
	path('online_consult/', views.online_consult),
	path('raw_material/', views.raw_mat),
	path('industrial_part/', views.indust_part),
	path('download/', views.download),
	path('engine_material/', views.engine_mat),
	path('BA/', views.BA),
]
