from . import views
from django.urls import path

app_name = 'pm'
urlpatterns = [
    
    path('dashboard/', views.dashboardView.as_view(), name='dashboard'),
    path('proyek/',views.proyek, name='proyek'),
    path('perangkat/', views.perangkatView.as_view(), name='perangkat'),
    path('list-organisasi/',views.listOrganisasiView.as_view(),name='list_organisasi'),
]