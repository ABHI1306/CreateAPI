from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, mobile, password=None, **extra_fields):
        if not mobile:
            raise ValueError("Mobile is reqired")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff True")
        return self.create_user(mobile, password, **extra_fields)

class User(AbstractUser):
    mobile = models.CharField(max_length = 15)

    #USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','mobile']

