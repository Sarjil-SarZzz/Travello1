from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,template_name='tour/home.html')

def packages(request):
    return render (request,template_name='tour/packages.html')

def login(request):
    return render (request,template_name='tour/login.html')



