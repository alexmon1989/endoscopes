from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.abstract_models import TimeStampedModel
from apps.accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField("Ім'я", max_length=30, blank=True)
    last_name = models.CharField("Прізвище", max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
