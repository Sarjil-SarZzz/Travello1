from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.

class Destination(models.Model):
    # destination_id = models.IntegerField()
    name = models.CharField(max_length=100)
    # location = models.CharField(max_length=200)
    # description = models.TextField(blank= True,null=True)

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='tour/home',null=True,blank=True)

    def __str__(self):
        return self.user.username
   

class Package(models.Model):
    title = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    duration = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='tour/package',blank=True,null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)    
    booking_date = models.DateField(auto_now_add=True)
    travel_date = models.DateField()
    status = models.CharField(max_length=100,choices=[
        ('confirmed','confirmed'),
        ('cancelled','cancelled'),
        ('pending','pending'),
    ]) 

    def __str__(self):
        return f"Booking{self.id} by {self.user.username}"
    

    


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    num_of_rooms =models.IntegerField()
    number_of_person = [
        ('1 Adult','1 Adult'),
        ('2 Adult','2 Adult'),
        ('3 Adult','3 Adult'),
    ]
    person = models.CharField(max_length=50,choices=number_of_person)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    check_in = models.DateField()    
    check_out = models.DateField()    
    

    def __str__(self):
        return self.name

class Flight(models.Model):
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    flight_number = models.CharField(max_length=20,unique=True)
    departure_airport = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='departure_flight_set')
    arrival_airport = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='arrival_flight_set')
    seat_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Flight{self.flight_number} by {self.provider_name}" 
    
class Flight_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)    
    booking_date = models.DateField(auto_now_add=True)
    travel_date = models.DateField()
    status = models.CharField(max_length=100,choices=[
        ('confirmed','confirmed'),
        ('cancelled','cancelled'),
        ('pending','pending'),
    ]) 

    def __str__(self):
        return f"Booking{self.id} by {self.user.username}"
    

class Bus(models.Model):
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    bus_number = models.CharField(max_length=20,unique=True)
    departure_station = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='departure_bus_set')
    arrival_station = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='arrival_bus_set')
    seat_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Bus{self.bus_number} by {self.provider_name}" 
    
class Car(models.Model):
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    pickup_location = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='pickup_car_set')
    dropoff_location = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='dropoff_car_set')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    car_number = models.CharField(max_length=20,unique=True)
    model_name = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Car{self.car_number} - {self.model_name} by {self.provider_name}"    



class Payment(models.Model):
    PAYMENT_METHOD = [
        ('credit_card','credit_card'),
        ('debit_card','debit_card'),
        ('paypal','paypal'),
        ('bank_transfer','bank_transfer'),
    ]
    
    PAYMENT_STATUS = [
        ('completed','completed'),
        ('pending','pending'),
        ('failed','failed'),
    ]

    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50,choices=PAYMENT_METHOD)
    payment_status = models.CharField(max_length=50,choices=PAYMENT_STATUS)
    transaction_id = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.payment_status}"


