"""
URL configuration for MyFirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from loginapp.views import *
from myapp1.views import myapp1
from myapp2.views import myapp2
from myapp3.views import myapp3
from myapp4.views import myapp4


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/",login),
    path("myapp1/",myapp1),
    path("myapp2/",myapp2),
    path("myapp3/",myapp3),
    path("myapp4/",myapp4),
    
    

]
