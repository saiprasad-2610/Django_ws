from django.shortcuts import render,HttpResponse

# Create your views here.
def myapp2(request):
    return HttpResponse("<h1>hello welcome... myapp2</h1   >")