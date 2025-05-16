"""
URL configuration for 后端 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('zc/', views.zc),
    path('index/', views.home),
    path('info/', views.info),
    path('echarts/', views.echarts),
    path('echarts1/', views.echarts1),
    path('echarts3/', views.echarts3),
    path('echarts4/', views.echarts4),
    path('echarts5/', views.echarts5),
]
