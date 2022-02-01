from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from shortuuidfield import ShortUUIDField

# Create your models here.

User = get_user_model()

class Ledger(models.Model):
    uuid = ShortUUIDField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    organisation = models.CharField(max_length=50, blank=True)
    created_on =  models.DateField()

    class Meta:
        verbose_name_plural = 'ledger'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"