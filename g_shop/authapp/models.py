from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ShopUser(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to='users_avatars', verbose_name="Аватар")
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)
