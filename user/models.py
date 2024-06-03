from django.db import models
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('repairman', 'Repairman'),
        ('admin', 'Admin'),
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='worker')
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"