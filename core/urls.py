from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.bot.urls')),  # Include app URLs
    path('admin/', admin.site.urls),
]
