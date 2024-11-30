from django.forms import ModelForm
from .models import *
from django import forms
from django.forms.widgets import FileInput

class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_img': FileInput(),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['travel_date']  # user can choose travel date others will be auto filled.



class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'


class FlightBookingForm(forms.ModelForm):
    class Meta:
        model = Flight_booking
        fields = ['travel_date']  # user can choose travel date others will be auto filled.  
