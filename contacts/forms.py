from django.forms import ModelForm, TextInput
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('uuid', 'owner', 'created_on', 'ledger',)
        widgets = {'phone_number': TextInput(attrs={
            'placeholder': '+234'
            })}