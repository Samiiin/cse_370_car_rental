from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def free_cars(request):
    cars = Car.objects.filter(car_status = "FREE")

    all_cars = []

    for car in cars:
        data = {
            "id": car.id,
            "name": car.name,
            "color": car.color,
            "year":car.year,
            "base_rate":car.base_rate
        }

        all_cars.append(data)
    
    return JsonResponse(all_cars,safe= False)
def all_cars(request):
    all_cars = Car.objects.all()
    details = []
    for car in all_cars:
        data={
            "id" : car.id,
            "name": car.name,
            "color": car.color,
            "year": car.year,
            "base_rate": car.base_rate
        }

        details.append(data)
    
    return JsonResponse(details,safe=False)
def all_customers(request):
    all_customers = CustomUser.objects.filter(is_admin= False)
    
    details = []
    for customer in all_customers:
        
        data={
            "id": customer.id,
            "phone_number": customer.phone_number,
            "email": customer.email,
            "address": customer.address,
            "reservations" : []

        }

        reservations = Reservation.objects.filter(customer = customer)

        for each in reservations:
            info = {
                "id":each.id,
                "status": each.status,
                "car":each.car.name,
                "pickup":each.pickup,
                "hours":each.hours,
            }

            data["reservations"].append(info)
        
        details.append(data)
    return JsonResponse(details,safe=False)
