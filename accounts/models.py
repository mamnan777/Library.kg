from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [('m', 'Мужской'), ('f', 'Женский')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='m')
    occupation = models.CharField(max_length=100, default='')
    bio = models.TextField(blank=True, default='')

    def str(self):
        return self.user.username