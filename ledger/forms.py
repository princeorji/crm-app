from django.forms import ModelForm, TextInput
from .models import Ledger

class AccountForm(ModelForm):
    class Meta:
        model = Ledger
        fields = '__all__'
        exclude = ('uuid', 'owner', 'created_on',)
        widgets = {'phone_number': TextInput(attrs={
            'placeholder': '+234'
            })}