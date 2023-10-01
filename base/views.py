from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Service, Business, BookService, Car, Customer
from datetime import datetime


def home(request):
    return render(request, "index.html")


def contact(request):
    return render(request, 'contact.html')


@login_required
def book_service(request):
    is_user_customer = Customer.objects.filter(user=request.user).exists()
    if is_user_customer:
        if request.method == "POST":
            data = request.POST
            car = data.get("car")
            service = data.get("service")
            details = data.get("details")
            date = data.get("date")
            deliver_date = datetime.strptime(date, "%m/%d/%Y")

            BookService.objects.create(
                client=request.user.customer,
                car=Car.objects.get(pk=int(car)),
                service=Service.objects.get(pk=int(service)),
                details=details,
                deliver_date=deliver_date
            )

        businesses = Business.objects.all()
        services_available = Service.objects.all()
        cars = request.user.customer.cars.all()
        bookings = request.user.customer.bookings.all()
        print(bookings.filter(acceptation=True).filter())
        context = {
            "providers": businesses,
            "services": services_available,
            "cars": cars,
            "bookings": bookings,
            'is_user_customer': is_user_customer
        }

    else:

        bookings = BookService.objects.filter(
            service__provider__user=request.user)
        pending_bookings = bookings.filter(cancelled=False)
        completed_bookings = bookings.filter(completed=True)
        print(f"Pending bookings are {pending_bookings}")

        context = {
            "bookings": bookings.filter(
                acceptation=True).filter(
                completed=False),
            'pending_bookings': pending_bookings.filter(
                completed=False).filter(
                    acceptation=False),
            'is_user_customer': is_user_customer,
            'completed_bookings': completed_bookings,
            'rejected_bookings': bookings.filter(
                cancelled=True)}
    return render(request, "dashboard.html", context)


def services(request):
    if request.method == "POST":
        pass
    return render(request, "service.html")


def about(request):
    return render(request, 'about.html')


def signin_page(request):
    return render(request, 'signinpage.html')


def cancel_booking(request, pk):
    booking = BookService.objects.get(pk=pk)
    booking.cancelled = True
    booking.save()
    return redirect("bookings")


def accept_booking(request, pk):
    booking = BookService.objects.get(pk=pk)
    booking.acceptation = True
    booking.save()
    return redirect("bookings")


def complete_booking(request, pk):
    booking = BookService.objects.get(pk=pk)
    booking.completed = True
    booking.save()
    return redirect("bookings")
