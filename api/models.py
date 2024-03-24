from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # Add your custom fields here
    phone_number = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    user = models.ForeignKey(user,on_delete = models.CASCADE,related_name = "customers")

class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length= 200)
    year = models.IntegerField()
    base_rate= models.DecimalField(decimal_places = 2, max_digits= 6)