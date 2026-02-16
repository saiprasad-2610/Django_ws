
from django.contrib import admin
from django.urls import path
from arithmetic_operations.views import *

urlpatterns = [
    path('', list),
    path('add/<int:n1>/<int:n2>/', addtwo),
    path('sub/<int:n1>/<int:n2>/', subtwo),
    path('mul/<int:n1>/<int:n2>/', multwo),
    path('div/<int:n1>/<int:n2>/', divtwo),
    
    path('square/<int:n1>/', square),
    path('cube/<int:n1>/', cube),
    
    path('check/<int:n1>/', checkNum),

    path('square-area/<int:side>/', square_area),
    path('rectangle-area/<int:l>/<int:b>/', rectangle_area),
    path('circle-area/<int:r>/', circle_area),
    path('fact/<int:n1>/', factorial),
    
    
]
