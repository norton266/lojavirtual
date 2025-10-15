from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/services/')),
    path('admin/', admin.site.urls),
    path('services/', include('lojavirtual.backend.services.urls')),
]
