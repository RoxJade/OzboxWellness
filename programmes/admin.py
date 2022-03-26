from django.contrib import admin
from .models import Category, Programmes

# Register your models here.


class ProgrammesAdmin(admin.ModelAdmin):
    '''returns programmes'''
    list_display = (
        'name',
        'category',
        'programme_length',
        'description',
        'programme_cost',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    '''returns category'''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Programmes)
admin.site.register(Category)
