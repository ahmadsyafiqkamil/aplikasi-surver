from django.urls import path
from . import views

urlpatterns = [
    path('dashboard_analis/',views.dashboard, name='dashboard_analis'),
    # path('organisasi/',views.organisasi, name='organisasi'),
    # path('perangkat/',views.perangkat, name='perangkat'),

    ]
