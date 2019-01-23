from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.index_login),
    path('signup/', views.signup),
    path('logout/', views.logout_view),
    path('logoutQues/', views.logout_ques),
]
