from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/disease-predictor/', views.disease_predictor_detail, name='disease_predictor_detail'),
    path('projects/spiffy/', views.spiffy_detail, name='spiffy_detail'),
    path('projects/shadow/', views.shadow_detail, name='shadow_detail'),
]
