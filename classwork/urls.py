"""classwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from classApplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^first_method/(?P<firstParametr>\D+)/',views.firt_method),
    # re_path(r'^second_method/(?P<secondParametr>\D+)/',views.secound_method),
    # re_path(r'^third_method/(?P<thirdParametr>\D+)/(?P<id>\d+)/',views.third_method),
    path('',views.Temp)
]
