from django import forms
from django.forms import ModelForm
from .models import Communication

class DateInput(forms.DateInput):
    input_type = 'date'

class CommunicationForm(ModelForm):
    class Meta:
        model = Communication
        fields = '__all__'
        exclude = ('uuid', 'owner', 'created_on', 'ledger',)
        widgets = {'date': DateInput}
            
