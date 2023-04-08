from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self.db)
        return user


class User(AbstractUser):
    objects = CustomUserManager() #менеджер моделей

    username = None
    # user_create_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE,
    #                                    **NULLABLE)
    email = models.EmailField(verbose_name='почта', unique=True)
    phone = models.CharField(max_length=50, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар')
    country = models.CharField(max_length=100, verbose_name='страна')
    email_confirmed = models.BooleanField(default=False)
    token = models.CharField(max_length=20, verbose_name='токен', **NULLABLE)
    token_expired = models.DateTimeField(**NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            (
                'change_status',
                'Can change is_staff'
            )
        ]
        unique_together = (
            ('email', 'phone'),
        )

