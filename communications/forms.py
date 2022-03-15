from django import forms
from django.forms import ModelForm, TextInput
from .models import Cummunication

class DateInput(forms.DateInput):
    input_type = 'date'

class CummunicationForm(ModelForm):
    class Meta:
        model = Cummunication
        fields = '__all__'
        exclude = ('uuid', 'owner', 'created_on', 'ledger',)
        widgets = {'phone_number': TextInput(attrs={
            'placeholder': '+234',
            }),
            'date': DateInput}
            
