"""
URL configuration for Travell_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Tour import views as t_views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', t_views.home,name = "home"),
    path('packages/',t_views.package, name = "packages"),
    path('payment/',t_views.payment, name = "payment"),
    path('hotel/',t_views.hotel, name = "hotel"),
    path('flights/',t_views.flights, name = "flights"),
    path('car/',t_views.car, name = "car"),
    path('bus/',t_views.bus, name = "bus"),
    path('bookings/',t_views.bookings,name = "bookings"),
    path('login/', t_views.login,name="login"),
    path('index/', t_views.index,name="index"),
    path('',t_views.signup,name="signup"),
    path('logout/',t_views.logout,name="logout"),


    path('create_package/',t_views.create_package,name="create_package"),
    path('update_package/<str:id>',t_views.update_package,name="update_package"),
    path('delete_package/<str:id>',t_views.delete_package,name="delete_package"),
    path('package_details/<str:id>',t_views.package_details,name="package_details"),

    path('profile_update/',t_views.profile_update,name="profile_update"),
    path('profile/',t_views.profile,name="profile"),

    path('book_package/<int:package_id>', t_views.book_package, name='book_package'),
    path('my_bookings/', t_views.user_bookings, name='my_bookings'),
    path('view_bookings/', t_views.flight_bookings, name='view_bookings'),


    path('create_flight/',t_views.create_flight,name="create_flight"),
    path('update_flight/<str:id>',t_views.update_flight,name="update_flight"),
    path('delete_flight/<str:id>',t_views.delete_flight,name="delete_flight"),
    path('flight_details/<str:id>',t_views.flight_details,name="flight_details"),

    path('book_flight/<int:flight_id>', t_views.book_flight, name='book_flight'),

    path('options/', t_views.options, name='options'),


    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
