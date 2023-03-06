from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from src.base.services import get_path_avatar, validate_size_image


class CustomUser(AbstractUser):

    ADMIN = 1
    SELLER = 2
    DEVELOP = 3
    EMPLOYEE = 4
    ROLES = (
        (ADMIN, 'Admin'),
        (SELLER, 'Seller'),
        (DEVELOP, 'Developer'),
        (EMPLOYEE, 'Employee'),
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLES, blank=True, null=True, default=4)
    avatar = models.ImageField(
        upload_to=get_path_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
