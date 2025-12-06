from django.urls import path
from . import views

urlpatterns = [
    path('recommendation/', views.crop_recommendation, name='crop_recommendation'),
    path('details/<str:crop_name>/', views.crop_details, name='crop_details'),
]