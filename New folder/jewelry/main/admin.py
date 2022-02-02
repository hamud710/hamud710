from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import *

# Register your models here.
@register(AboutUs)
class PersonAdmin(ModelAdmin):
    list_display = ('Name', 'Email', 'Phone')
    icon_name = 'view_carousel'