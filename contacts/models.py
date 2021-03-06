from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from shortuuidfield import ShortUUIDField

from ledger.models import Ledger

# Create your models here.

User = get_user_model()

class Contact(models.Model):
    uuid = ShortUUIDField(unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    role = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    ledger = models.ForeignKey(Ledger, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on =  models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
