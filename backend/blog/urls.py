from django.urls import path

from blog import views

urlpatterns = [
    path('blogs/', views.BlogGetCreateView.as_view())
]
