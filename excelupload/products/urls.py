from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',ProductViews.as_view(),name='product'),
    path('add/',ProductViews.as_view(),name='add product'),
    path('sales/',SalesProduct.as_view(),name='sales'),
    path('sales/month/',SalesMonthProduct.as_view(),name='sales per month'),

    
    path('share/',ShareDivision.as_view(),name='share'),
    path('events/',CalendarData.as_view(),name='event...'),

    path('events/add/',CalendarData.as_view(),name='event...'),
    path('events/delete/<int:pk>/',DeleteOrder.as_view(),name='event delete'),
    path('events/update/<int:pk>/',DeleteOrder.as_view(),name='event update'),
]