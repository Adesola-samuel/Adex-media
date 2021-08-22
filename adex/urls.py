from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('page.urls')),
    path('house/', admin.site.urls),
]
