from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('example/<str:entity_name>', views.main_page),
]
