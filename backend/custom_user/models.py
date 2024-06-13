from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_no, email, password, **kwargs):
        user = self.model(phone_no=phone_no, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_no, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        self.create_user(phone_no, email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(unique=True, max_length=10)
    city = models.CharField(max_length=40)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "phone_no"
    objects = CustomUserManager()
