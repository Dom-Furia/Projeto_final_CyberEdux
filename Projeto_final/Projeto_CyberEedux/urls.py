
from django.contrib import admin
from django.urls import path
from sistema_academico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_world, name='hello_world'),
]
