from django.http.response import HttpResponse
from django.http.request import HttpRequest
import random

def hello_view(request, name):
    return HttpResponse(f"Hello {name}!")
def roll_die_view(request, sides):
    return HttpResponse(random.randint(1, sides))
def rand_view(request, lo, hi):
    return HttpResponse(random.randint(lo, hi))
def add_view(request, a, b):
    return HttpResponse(a+b)