from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Custom model manager for UserProfile"""

    def create_user(self, email, name, password=None, **kwargs):
        """Change New User Profile Function"""
        if not email:
            raise ValueError('User Must Have an Email Address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password,  **kwargs):
        '''Create and save superuser'''
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, name, password, **kwargs)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for overriding users in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name Of User"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name Of User"""
        return self.name

    def __str__(self):
        """Return str rep"""
        return self.email
