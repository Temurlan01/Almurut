from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager



class CustomUser(AbstractUser):
    from market.models import Product

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, db_index=True)

    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to="avatars/")
    phone_number = models.CharField(max_length=25)
    favorites_product = models.ManyToManyField(Product)
    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

