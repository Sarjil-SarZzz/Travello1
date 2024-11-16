from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render (request,template_name='tour/home.html')

def login(request):
    return render (request,template_name='tour/login.html')

def package(request):
    package = Package.objects.all()
    context = {
        'package': package,
    }
    return render (request,template_name='tour/packages.html',context = context)

def bookings(request):
    booking= Booking.objects.all()
    context = {
        'booking': booking,
    }
    return render (request,template_name='tour/bookings.html',context = context)

def payment(request):
    payment= Payment.objects.all()
    context = {
        'payment': payment,
    }
    return render (request,template_name='tour/payment.html',context = context)

def car(request):
    car= Car.objects.all()
    context = {
        'car': car,
    }
    return render (request,template_name='tour/car.html',context = context)

def bus(request):
    bus= Bus.objects.all()
    context = {
        'bus': bus,
    }
    return render (request,template_name='tour/bus.html',context = context)

def flights(request):
    flight= Flight.objects.all()
    context = {
        'flight': flight,
    }
    return render (request,template_name='tour/flights.html',context = context)

def hotel(request):
    hotel= Hotel.objects.all()
    context = {
        'hotel': hotel,
    }
    return render (request,template_name='tour/hotel.html',context = context)





