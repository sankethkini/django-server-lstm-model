from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('abc',views.getCPUUsage,name='cpu_usage')
]

