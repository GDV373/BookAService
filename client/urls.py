from django.urls import path
from .views import car_crud, customer_profile, customer_profile_update
from authentication.views import (
    custom_500_handler,
    custom_error_handler
)

handler500 = 'authentication.views.custom_500_handler'
handler404 = 'authentication.views.custom_error_handler'
handler500 = 'authentication.views.custom_500_handler'
handler404 = 'authentication.views.custom_error_handler'


urlpatterns = [
    path("cars/", car_crud, name="car_list"),
    path(
        "cars/create/",
        lambda request: car_crud(request, action="create"),
        name="car_create",
    ),
    path(
        "cars/<str:pk>/update/",
        lambda request, pk: car_crud(request, pk=pk, action="update"),
        name="car_update",
    ),
    path(
        "cars/<str:pk>/delete/",
        lambda request, pk: car_crud(request, pk=pk, action="delete"),
        name="car_delete",
    ),
    path(
        "client_settings/",
        lambda request, pk: car_crud(request, pk=pk, action="delete"),
        name="client_settings",
    ),
    path("customer_profile/", customer_profile, name="customer_profile"),
    path(
        "customer_profile_update/<str:pk>/update/",
        customer_profile_update,
        name="customer_profile_update",
    ),
]
