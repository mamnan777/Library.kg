from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    city = models.CharField(max_length=50)

    def str(self):
        return self.user.username