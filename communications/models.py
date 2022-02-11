from enum import unique
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from shortuuidfield import ShortUUIDField

from ledger.models import Ledger

# Create your models here.

User = get_user_model()

class Cummunication(models.Model):
    TYPE = (
        (1, 'Meeting'),
        (2, 'Phone'),
        (3, 'Email'),
    )
    uuid = ShortUUIDField(unique=True)
    subject = models.CharField(max_length=50)
    notes = models.TextField()
    kind = models.PositiveSmallIntegerField(choices=TYPE)
    date = models.DateField()
    ledger = models.ForeignKey(Ledger, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on =  models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject