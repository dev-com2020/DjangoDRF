
from django.contrib import admin
from django.urls import path, include

from backend.blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo_app.urls')),
    path('api/', include('blog.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path("verify/", views.verify_blog)
]
