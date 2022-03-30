from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField


class User(AbstractUser):
    GENDER_CHOICE = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )
    profile_image = ResizedImageField(
        upload_to='accounts/images/profiles/', null=True, blank=True, size=[200, 200], quality=75, force_format='PNG',
        help_text='size of logo must be 100*100 and format must be png image file', crop=['middle', 'center']
    )
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICE)
    about = models.TextField(null=True, blank=True, help_text="Tell us something interesting about yourself")
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
