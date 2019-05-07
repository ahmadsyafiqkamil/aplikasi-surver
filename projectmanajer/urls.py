from . import views
from django.urls import path

app_name = 'pm'
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('proyek/',views.proyek, name='proyek'),
    path('perangkat/',views.perangkat, name='perangkat'),

]