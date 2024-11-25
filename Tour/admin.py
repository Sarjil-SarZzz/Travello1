from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Destination)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Hotel)
admin.site.register(Flight)
admin.site.register(Bus)
admin.site.register(Car)
admin.site.register(Payment)
admin.site.register(Profile)

