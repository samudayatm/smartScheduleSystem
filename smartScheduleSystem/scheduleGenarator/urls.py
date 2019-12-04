from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.process, name='saveData'),
    path('process', views.process, name='process'),
]
