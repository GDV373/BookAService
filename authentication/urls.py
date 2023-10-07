from django.urls import path
from authentication.views import (
    loginView, delete_account, register_client, register_business,
    logout_view, edit_profile, password_update, custom_500_handler,
    custom_error_handler
)

handler500 = 'authentication.views.custom_500_handler'
handler404 = 'authentication.views.custom_error_handler'

urlpatterns = [
    path('login/', loginView, name="login"),
    path('delete_account/', delete_account, name="delete_account"),
    path('register_client/', register_client, name="register_client"),
    path('register_business/', register_business, name="register_business"),
    path('logout/', logout_view, name="logout"),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('password_update/', password_update, name='password_update'),
]

