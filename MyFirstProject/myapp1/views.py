from django.shortcuts import render,HttpResponse

# Create your views here.
def myapp1(request):
    return HttpResponse("<h1>hello welcome... myapp1</h1   >")
