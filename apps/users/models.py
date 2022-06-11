from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class CustomAuthUserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'users'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_last_name = models.CharField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    role = models.CharField(max_length=16, default='user')
    is_active = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)

    is_superuser = None
    groups = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
