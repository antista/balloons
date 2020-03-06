from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('example/<str:entity_name>', views.main_page),
    path('example/static/styles/images/entities/<str:image_name>', views.redirect_pictures),
    path('balloons_counter/static/styles/images/entities/<str:image_name>', views.redirect_pictures),
    path('example/balloons_counter/static/styles/images/entities/<str:image_name>', views.redirect_pictures),
]
