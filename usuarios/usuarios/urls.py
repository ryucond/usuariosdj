
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls', namespace='users')),
    path('', include('applications.home.urls', namespace='home')),
]
