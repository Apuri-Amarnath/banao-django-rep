from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.doctor_signup, name='doctor_signup'),
    path('signin/', views.doctor_login, name='doctor_login'),
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('logout/', views.doctor_logout, name='doctor_logout'),
]
