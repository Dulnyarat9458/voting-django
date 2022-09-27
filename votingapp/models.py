
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    """ User Manager that knows how to create users via email instead of username """

    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, first_name=None, last_name=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_user(self, email=None, password=None, first_name=None, last_name=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)


class User(AbstractUser):
    objects = UserManager()
    REQUIRED_FIELDS = ['first_name', 'last_name','phone']
    USERNAME_FIELD = "email"
    username = None
    phone = PhoneNumberField(blank=True,region="TH", null=False, unique=True)
    email = models.EmailField(
        "Email", blank=False, null=False, unique=True)
    votable_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.get_full_name()


class Choice(models.Model):
    upload_pic = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=80)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name