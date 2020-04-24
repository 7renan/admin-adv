from django.forms.models import ModelForm
from contacts.models import Contact


class ContactFormCreate(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone')
