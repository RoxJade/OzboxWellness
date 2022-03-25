from django.contrib import admin
from .models import Category, Programmes

# Register your models here.
admin.site.register(Programmes)
admin.site.register(Category)
