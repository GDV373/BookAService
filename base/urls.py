#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
from views import *

urlpatterns = [
    path('bookings/', book_service, name='bookings'),
    path('', home, name='dashboard'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('signinpage/', signin_page, name='signinpage'),
    path('cancel_booking/<str:pk>/', cancel_booking,
         name='cancel_booking'),
    path('accept_booking/<str:pk>/', accept_booking,
         name='accept_booking'),
    path('complete_booking/<str:pk>/', complete_booking,
         name='complete_booking'),
    ]
