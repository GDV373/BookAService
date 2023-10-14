from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CarForm, CarCreateForm, CustomerForm
from accounts.models import Car, Customer


def custom_500_handler(request, exception=None):
    return render(request, 'page_404.html', status=500)


def custom_error_handler(request, exception=None):
    if exception is None:
        return render(request, 'page_404.html', status=404)
    else:
        return render(request, 'page_404.html', status=404)


@login_required
def car_crud(request, pk=None, action=None):
    car = None

    # For creating a new car
    if action == 'create':
        if request.method == 'POST':
            form = CarCreateForm(request.POST)
            if form.is_valid():
                new_car = form.save(commit=False)
                new_car.owner = request.user.customer
                new_car.save()
                return redirect('car_list')
        else:
            form = CarCreateForm()
            return render(request, 'cars/car_create.html', {'form': form})

    elif action == 'update':
        car = get_object_or_404(Car, pk=pk, owner=request.user.customer)
        if request.method == 'POST':
            form = CarCreateForm(request.POST, instance=car)
            if form.is_valid():
                form.save()
                return redirect('car_list')
        else:
            form = CarCreateForm(instance=car)
            return render(request, 'cars/car_update.html', {'form': form})

    # For deleting a car
    elif action == 'delete':
        car = get_object_or_404(Car, pk=pk, owner=request.user.customer)
        car.delete()
        return redirect('car_list')

    # For listing all cars
    else:
        cars = Car.objects.filter(owner=request.user.customer)
        return render(request, 'cars/manage_cars.html', {'cars': cars})

    return render(request, 'cars/manage_cars.html', {'car': car})


@login_required
def customer_profile(request):
    return render(request, 'client_profile.html')


@login_required
def customer_profile_update(request, pk):
    business = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            return redirect('customer_profile')
    else:
        form = CustomerForm(instance=business)
    return render(request, 'client_profile_update.html', {'form': form})
