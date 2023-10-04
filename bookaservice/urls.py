from django.contrib import admin
from django.urls import path, include

handler505 = 'authentication.views.custom_505_handler'
handler404 = 'authentication.views.custom_error_handler'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('base.urls')),
    path('', include('client.urls')),
    path('', include('business.urls')),
]