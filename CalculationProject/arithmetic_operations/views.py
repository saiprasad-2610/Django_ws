from django.shortcuts import render, HttpResponse

# Create your views here.
def addtwo(request, n1, n2):
    return HttpResponse(f"<h1>Addition of {n1} + {n2} is {n1+n2}</h1>")

def subtwo(request, n1, n2):
    return HttpResponse(f"<h1>Subtraction of {n1} - {n2} is {n1-n2}</h1>")

def multwo(request, n1, n2):
    return HttpResponse(f"<h1>Multiplication of {n1} x {n2} is {n1*n2}</h1>")

def divtwo(request, n1, n2):
    return HttpResponse(f"<h1>Division of {n1} / {n2} is {n1/n2}</h1>")

def square(request, n1):
    return HttpResponse(f"<h1>Square of {n1} is {n1**2}</h1>")

def cube(request, n1):
    return HttpResponse(f"<h1>Cube of {n1} is {n1**3}</h1>")

def checkNum(request, n1):
    if n1 % 2 == 0:
        return HttpResponse(f"<h1>{n1} is an Even Number</h1>")
    else:
        return HttpResponse(f"<h1>{n1} is an Odd Number</h1>")

def square_area(request, side):
    return HttpResponse(f"<h1>Side is {side}, and Area Of Square is {side**2}</h1>")

def rectangle_area(request, l, b):
    return HttpResponse(f"<h1>Length is {l}, Breadth is {b} and Area Of Rectangle is {l*b}</h1>")

def circle_area(request, r):
    return HttpResponse(f"<h1>Radius is {r}, and Area Of Circle is {3.14*r**2}</h1>")

def factorial(request,n1):
    fact = 1
    for i in range(1,n1+1):
        fact = fact*i
    return HttpResponse(f"<h1> Factorial of {n1} is {fact}</h1>")
    


from django.http import HttpResponse
from django.http import HttpResponse

def list(request):
    return HttpResponse("""
    <h1>Available URL</h1>
    <h2><ul>
        <li>add/</li>
        <li>sub/</li>
        <li>mul/</li>
        <li>div/</li>
        <li>square/</li>
        <li>cube/</li>
        <li>check</li>
        <li>square-area/</li>
        <li>rectangle-area/</li>
        <li>circle-area/</li>
        <li>fact/</li>
    </ul></h2>
    """)

