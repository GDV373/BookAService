from django.contrib import admin
from .models import Customer, Business, Car, User, BookService, Service


admin.site.register(User)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(BookService)
admin.site.register(Service)
