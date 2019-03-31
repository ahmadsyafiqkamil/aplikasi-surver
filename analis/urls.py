from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('organisasi/',views.organisasi, name='organisasi'),
    path('perangkat/',views.perangkat, name='perangkat'),

    ]
