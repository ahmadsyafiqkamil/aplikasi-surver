from . import views
from django.urls import path, include

urlpatterns = [
    path('dashboard_surveyor/',views.dashboard, name='dashboard_surveyor'),

]
