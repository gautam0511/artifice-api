from django.contrib import admin

# Register your models here.

from .models import Productmodel,Calendarmodel
admin.site.register(Productmodel)
admin.site.register(Calendarmodel)