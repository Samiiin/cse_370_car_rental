from django.urls import path,include 
from . import views 

urlpatterns = [
    #Customer Dashbaord
    path("free_cars",views.free_cars,name="free_cars"),

    #Admin Dashboard
    path("all_cars",views.all_cars,name="all_cars"),
    path("all_customers", views.all_customers, name="all_customers"),
    #path("all_reservations",views.all_reservations, name="all_reservations")

    
]