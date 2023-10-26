from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def hey_view(request:HttpRequest, name:str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")
def age_view(request:HttpRequest, end:int, year:int) -> HttpResponse:
    age = end-year
    return HttpResponse(f"{age}")
def order_view(request:HttpRequest, burgers:int, fries:int, drinks:int) -> HttpResponse:
    btotal = burgers * 4.5
    ftotal = fries * 1.5
    dtotal = drinks * 1
    total = btotal + ftotal + dtotal
    return HttpResponse(f"{str(total)}")
