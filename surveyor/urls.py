from . import views
from django.urls import path, include

urlpatterns = [
    path('analis',views.dashboard, name='dashboard_surveyor'),

]
