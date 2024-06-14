from django.urls import path

from blog import views

urlpatterns = [
    path('blogs/', views.BlogGetCreateView.as_view()),
    path('blogs/<int:pk>', views.BlogGetUpdateDestroyView.as_view()),
    path('find/', views.get_blogs_by_author),
]
