from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)  # Активный, Спокойный, Семейный

    def str(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=100)  # Поход в горы, Поездка на море, Баня
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    # многие ко многим
    categories = models.ManyToManyField(Category, related_name='tours')

    def str(self):
        return self.title


# 1 ко многим: у тура много комментариев
class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.author}: {self.tour}'


# 1 к 1: один человек, одно бронирование
class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='booking')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user} → {self.tour}'