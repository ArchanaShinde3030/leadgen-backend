from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # हे Import करा



urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/', include('leads.urls')),
]
