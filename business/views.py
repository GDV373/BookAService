from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Service
from accounts.models import Business
from .forms import BusinessForm
from authentication.views import (
    custom_500_handler,
    custom_error_handler
)


def custom_500_handler(request, exception=None):
    return render(request, 'page_404.html', status=500)


def custom_error_handler(request, exception=None):
    if exception is None:
        return render(request, 'page_404.html', status=404)
    else:
        return render(request, 'page_404.html', status=404)


@login_required
def service_crud(request, pk=None, action=None):
    """These views collectively manage user authentication,
    business profile updates, and service CRUD operations
    in the web application."""
    services = None
    if action == 'create':
        if request.method == 'POST':
            name = request.POST.get("name")
            service = Service.objects.create(
                name=name,
                provider=request.user.business)

        else:
            return render(request, 'services/service_create.html')

    elif action == 'update':
        service = get_object_or_404(
            Service,
            pk=pk,
            provider=request.user.business)
        if request.method == 'POST':
            name = request.POST.get("name")
            service.name = name
            service.save()

        else:
            return render(
                request,
                'services/service_update.html',
                {"service": service})

    elif action == 'delete':
        service = get_object_or_404(
            Service,
            pk=pk,
            provider=request.user.business)
        service.delete()
        return redirect('service_list')

    services = Service.objects.filter(provider=request.user.business)
    return render(
        request,
        'services/manage_services.html',
        {'services': services})


@login_required
def business_list(request):
    return render(request, 'business_profile.html')


@login_required
def business_update(request, pk):
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            return redirect('business_profile')
    else:
        form = BusinessForm(instance=business)
    return render(request, 'business_profile_update.html', {'form': form})
