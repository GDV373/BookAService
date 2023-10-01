#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
from views import *

urlpatterns = [
    path('manage_services/', service_crud, name='service_list'),
    path('manage_services/create/', lambda request: \
         service_crud(request, action='create'), name='service_create'
         ),
    path('manage_services/<str:pk>/update/', lambda request, pk: \
         service_crud(request, pk=pk, action='update'),
         name='service_update'),
    path('manage_services/<str:pk>/delete/', lambda request, pk: \
         service_crud(request, pk=pk, action='delete'),
         name='service_delete'),
    path('business_settings/', lambda request, pk: \
         service_crud(request, pk=pk, action='delete'),
         name='business_settings'),
    path('business_profile/', business_list, name='business_profile'),
    path('business_profile/<str:pk>/update/', business_update,
         name='business_profile_update'),
    ]
