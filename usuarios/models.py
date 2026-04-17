from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('internal', 'Internal'),
        ('public', 'Public'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='public')

    def is_internal(self):
        return self.role == 'internal'

    def is_public(self):
        return self.role == 'public'
