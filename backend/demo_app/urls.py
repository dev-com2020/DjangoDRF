from django.urls import path
from demo_app import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('hello_drf/', views.hello_world_drf),
]
