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


from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def register(request):
    pass

def change_password(request):
    pass

def reset_password(request):
    pass

def view_car_details(request, car_id):
    car = Car.objects.get(id=car_id)
    data = {
        "car_id": car.id , 
        "name": car.name,
        "color" : car.color,
        "year" : car.year,
        "base_rate": car.base_rate,
        "car_status" :  car.car_status,
    }
    return JsonResponse(data)

    




def reserve_car(request, car_id):
    pass

def cancel_reservation(request, reservation_id):
    pass

def make_payment(request, reservation_id):
    pass

def view_payment_history(request):
    all_payments = Payment.objects.all()
    data = []
    for payment in all_payments:
        info = {
            "customer" : payment.customer.username,
            "reservation" : str(payment.reservation),
            "payment_status" : payment.payment_status,
            "payment_method" : payment.payment_method,
        
        }
        data.append(info)
    return JsonResponse(data,safe = False)


def view_payment_details(request, payment_id):
    pass 
def view_profile(request):
    pass

def edit_profile(request):
    pass

def view_reservations(request):
    pass

def modify_reservation(request, reservation_id):
    pass

def cancel_reservation(request, reservation_id):
    pass

def add_car(request):
    pass

def edit_car_details(request, car_id):
    pass

def delete_car(request, car_id):
    pass

def all_reservations_admin(request):
    pass

def view_reservation_admin(request, reservation_id):
    pass

def all_payments_admin(request):
    pass

def view_payment_admin(request, payment_id):
    pass

def view_customer_admin(request, customer_id):
    pass 