from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import *

from .decorators import unauthenticated_user,allowed_users,admin_only
# Create your views here.
@login_required(login_url='login')
def home(request):
        if request.user.is_authenticated:
            print("User is logged in")
        else:
            print("User is not logged in")

        return render (request,template_name='tour/home.html')


def package(request):
    package = Package.objects.all()
    context = {
        'package': package,
    }
    return render (request,template_name='tour/packages.html',context = context)

def bookings(request):
    booking= Booking.objects.get(pk=id)
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

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()

            group = Group.objects.get(name='customers')  # Ensure the 'customer' group exists
            my_user.groups.add(group)
            return redirect('login')
    return render(request,'registration/signup.html')    
      
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")   
    return render (request,template_name='registration/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')


def index(request):
    return render(request,template_name='tour/index.html')

@allowed_users(allowed_roles=['admin'])
@admin_only
def create_package(request):
    form = PackageForm()
    if request.method == 'POST':
        form = PackageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('packages')
    context = {'form':form}
    return render(request, template_name='tour\package_form.html',context=context)


def update_package(request,id):
    package = Package.objects.get(pk = id)
    form = PackageForm(instance= package)
    if request.method == 'POST':
        form = PackageForm(request.POST,request.FILES,instance=package)
        if form.is_valid():
            form.save()
            return redirect ('packages')
    context = {'form':form}
    return render(request, template_name='tour\package_form.html',context=context)

def package_details(request,id):
    package = Package.objects.get(pk=id)
    context = {
        'package':package,
    }
    return render(request,template_name='tour\package_details.html',context=context)

def delete_package(request,id):
    package = Package.objects.get(pk=id)
    if request.method == 'POST':
        package.delete()
        return redirect('packages')
    return render(request,template_name='tour\delete_package.html')



def profile(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile,
    }
    return render (request,template_name='tour/profile.html',context = context)

def profile_update(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request,f'{username},Your profile is updated.')
            return redirect ('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render (request,template_name='tour/profile_update.html',context=context)  


def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the logged-in user to the booking
            booking.package = package   # Assign the selected package
            booking.status = 'pending'  # Default status
            booking.save()
            return HttpResponse("your bookings is successful!!!")  
            # return redirect('book_package', package_id=package.id)
    else:
        form = BookingForm()
    
    return render(request, 'tour/book_package.html', {'form': form, 'package': package})


def user_bookings(request):
    # Fetch bookings for the logged-in user
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'tour/my_bookings.html', {'bookings': user_bookings})



def flight_details(request,id):
    flight = Flight.objects.get(pk=id)
    context = {
        'flight':flight,
    }
    return render(request,template_name='tour/flight_details.html',context=context)



def create_flight(request):
    form = FlightForm()
    if request.method == 'POST':
        form = FlightForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('flights')
    context = {'form':form}
    return render(request, template_name='tour/flight_form.html',context=context)



def update_flight(request,id):
    flight = Flight.objects.get(pk = id)
    form = FlightForm(instance= flight)
    if request.method == 'POST':
        form = FlightForm(request.POST,request.FILES,instance=flight)
        if form.is_valid():
            form.save()
            return redirect ('flights')
    context = {'form':form}
    return render(request, template_name='tour/flight_form.html',context=context)


def delete_flight(request,id):
    flight = Flight.objects.get(pk=id)
    if request.method == 'POST':
        flight.delete()
        return redirect('flights')
    return render(request,template_name='tour/delete_flight.html')


def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if request.method == "POST":
        form = FlightBookingForm(request.POST)
        if form.is_valid():
            Flight_booking = form.save(commit=False)
            Flight_booking.user = request.user  # Assign the logged-in user to the Flight_booking
            Flight_booking.flight = flight   # Assign the selected package
            Flight_booking.status = 'pending'  # Default status
            Flight_booking.save()
            return HttpResponse("Your booking is successful!")
           
    else:
        form = FlightBookingForm()
    
    return render(request, 'tour/book_flight.html', {'form': form, 'flight': flight})


def flight_bookings(request):
    # Fetch bookings for the logged-in user
    user_bookings = Flight_booking.objects.filter(user=request.user)
    return render(request, 'tour/view_bookings.html', {'bookings': user_bookings})


def options(request):
    return render (request,template_name='tour/options.html')


