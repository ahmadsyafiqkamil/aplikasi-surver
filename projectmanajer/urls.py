from . import views
from django.urls import path

urlpatterns = [
    path('dashboard_pm/',views.dashboard, name='dashboard_pm'),
    path('proyek/',views.dashboard, name='proyek_pm'),
    path('perangkat/',views.dashboard, name='perangkat_pm'),

]
