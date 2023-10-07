from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class RequestingOrder(models.Model):
    MY_CHOICES = (
        ('FDS', 'FUEL DELIVERY'),
        ('EOS', 'ENGINE OIL SERVICE'),
        ('CWS', 'CAR WASH SERVICE'),
        ('BSS', 'BATTERY SERIVCE'),
        ('TS', 'TYRE SERVICE'),
        ('TTS', 'TOW TRUCK SERVICE'),
    )
    brand_model = models.CharField(max_length=100)
    check_username = models.TextField(null=True)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    car_id = models.CharField(max_length=10)
    note = models.TextField(max_length=250)
    the_service = models.CharField(max_length=20, choices=MY_CHOICES)
    

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%y/%m/%d' ,default='def.jpeg')
    nation = models.CharField(max_length=100, default='')
    about_the_user = models.TextField(max_length=50, null=True)
    adress = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    postal_code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Ordershistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(RequestingOrder, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order ID: {self.id}, Car: {self.car.brand_model}, Date Created: {self.date_created}"




