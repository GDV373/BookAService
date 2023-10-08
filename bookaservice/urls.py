from django.contrib import admin
from django.urls import path, include
from authentication.views import (
    custom_500_handler,
    custom_error_handler
)

handler500 = 'authentication.views.custom_500_handler'
handler404 = 'authentication.views.custom_error_handler'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('base.urls')),
    path('', include('client.urls')),
    path('', include('business.urls')),
]
