from django.shortcuts import render, redirect
from accounts.models import Customer, Business
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from accounts.models import Locations
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

User = get_user_model()


@login_required
def logout_view(request):
    """These views collectively handle various aspects of user
    authentication, registration, and profile management, and
    provide custom error handling for the application."""
    logout(request)
    return redirect("dashboard")


def loginView(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, 'Invalid Email or Password.')

    return render(request, "signin.html")


def delete_account(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect("dashboard")


def custom_500_handler(request, exception=None):
    return render(request, 'page_404.html', status=500)


def custom_error_handler(request, exception=None):
    if exception is None:
        return render(request, 'page_404.html', status=404)
    else:
        return render(request, 'page_404.html', status=404)

def register_client(request):
    locations = Locations.Malta_Locations
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        var_number = request.POST.get("vat")
        location = request.POST.get("location")
        id_number = request.POST.get("id_number")
        mobile_number = request.POST.get("number")
        address = request.POST.get("address")

        if password == password2:
            try:
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name)
                user.save()
                Customer.objects.create(
                    user=user,
                    Location=location,
                    ID_number=id_number,
                    Mobile=mobile_number,
                    Address=address,
                    Vat_Number=var_number
                )

                user = authenticate(request, email=email, password=password)
                login(request, user)
                return redirect("dashboard")
            except IntegrityError:
                messages.error(request, 'User Already Existed.')

        else:
            messages.error(request, 'Password Does Not Match')

        return render(request, "register.html", {"locations": locations})

    return render(request, "register.html", {"locations": locations})


def register_business(request):
    locations = Locations.Malta_Locations
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        location = request.POST.get("location")
        var_number = request.POST.get("vat")
        business_name = request.POST.get("business_name")
        mobile_number = request.POST.get("number")
        address = request.POST.get("address")

        if password == password2:
            try:
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name)
                user.save()
                Business.objects.create(
                    user=user,
                    Location=location,
                    name=business_name,
                    Mobile=mobile_number,
                    Address=address,
                    Vat_Number=var_number
                )

                user = authenticate(request, email=email, password=password)
                login(request, user)
                return redirect("dashboard")

            except IntegrityError:
                messages.error(request, 'User Already Existed.')

        else:
            messages.error(request, 'Password Does Not Match!')

        return render(
            request, "register_business.html", {
                "locations": locations})

    return render(request, "register_business.html", {"locations": locations})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            if request.user.is_customer():
                return redirect('customer_profile')
            return redirect('business_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'user_profile_update.html', {'form': form})


@login_required
def password_update(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Important to update the session with the new password hash
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password has been changed successfully.')
            if request.user.is_customer():
                return redirect('customer_profile')
            return redirect('business_profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_update.html', {'form': form})
