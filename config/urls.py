from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', include('apps.movies.api.v1.urls')),
] 