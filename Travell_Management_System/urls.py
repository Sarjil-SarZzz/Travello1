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
from django.urls import path
from Tour import views as t_views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', t_views.home,name = "home"),
    path('package/',t_views.package, name = "package"),
    path('login/',t_views.login, name = "login"),
    path('payment/',t_views.payment, name = "payment"),
    path('hotel/',t_views.hotel, name = "hotel"),
    path('flights/',t_views.flights, name = "flights"),
    path('car/',t_views.car, name = "car"),
    path('bus/',t_views.bus, name = "bus"),
    path('bookings/',t_views.bookings,name = "bookings"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
