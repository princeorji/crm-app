from django.forms import ModelForm, TextInput
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {'phone_number': TextInput(attrs={
            'placeholder': '+234'
            })}