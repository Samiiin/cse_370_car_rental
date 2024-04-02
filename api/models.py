from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # Add your custom fields here
    phone_number = models.CharField(max_length=255,default = "")
    address = models.TextField(blank = True,null = True)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    
class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length= 200)
    year = models.IntegerField()
    base_rate= models.DecimalField(decimal_places = 2, max_digits= 6)
    STATUS_CHOICES = [
        ('BOOKED', 'Booked'),
        ('FREE', 'Free'),]
    car_status =  models.CharField(max_length=20, choices=STATUS_CHOICES, default='FREE')

    def __str__(self):
        return f"{self.color} {self.name} {self.year}"
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('BOOKED', 'Booked'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'), 
        ('CANCELLED', 'Cancelled'),
    ]

    # Define fields for the reservation model
    # Other fields go here like user, date, etc.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='BOOKED')

    car = models.ForeignKey(Car,on_delete = models.CASCADE, related_name = 'reservations')
    customer = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name = 'reservations')
    pickup = models.DateTimeField()
    hours = models.IntegerField(default = 1)
    def __str__(self):
        return f"{self.id}:{self.car.name} for {self.customer.username}"

class Payment(models.Model):
    customer = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name = 'payments')
    reservation = models.ForeignKey(Reservation,on_delete = models.CASCADE, related_name = 'payments')
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled'),
    ]

    # Define fields for the reservation model
    # Other fields go here like user, date, etc.
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    PAYMENT_METHOD_CHOICES = [
        ('CARD',"Card"), 
        ('CASH', 'Cash'),
        ('BKASH', 'Bkash'),
    ]

    # Define fields for the reservation model
    # Other fields go here like user, car, rental dates, etc.
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    def __str__(self):
        return f"{self.id}:payment for {self.customer.username} payment_status : {self.payment_status}"