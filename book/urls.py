from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('writers/', views.my_favourite_writers, name='my_favourite_writers'),
    path('sayings/', views.sayings_of_great_poets, name='sayings_of_great_poets'),
]