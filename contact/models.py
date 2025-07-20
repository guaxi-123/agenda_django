from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True, verbose_name='Show in list')
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}".strip()

