from django.contrib import admin
from .models import Category, Tour, Comment, Booking

admin.site.register([Category, Tour, Comment, Booking])