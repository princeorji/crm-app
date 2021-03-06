from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from shortuuidfield import ShortUUIDField

# Create your models here.

User = get_user_model()

class Ledger(models.Model):
    uuid = ShortUUIDField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_on =  models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ledger'

    def __str__(self):
        return self.name