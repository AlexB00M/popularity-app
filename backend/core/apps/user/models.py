from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, telegram_id, user_name, password=None):
        if not telegram_id:
            raise ValueError("Users must have a telegram_id")
        user = self.model(
            telegram_id=telegram_id, 
            user_name=user_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, telegram_id, user_name=None, password=None):
        user = self.create_user(
            telegram_id=telegram_id,
            user_name=user_name,
            password=password,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    # User data
    telegram_id = models.BigIntegerField(unique=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Сomparison with tables
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)

    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name or str(self.telegram_id)
