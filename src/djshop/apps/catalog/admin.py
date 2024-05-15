from django.contrib import admin
from djshop.apps.catalog.models import *


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_filter = ('title', 'price')
    search_fields = ('title',)



