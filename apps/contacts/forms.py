from django.forms.models import ModelForm
from apps.contacts.models import Contact, Phone


class ContactFormCreate(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone')


class PhoneFormCreate(ModelForm):
    class Meta:
        model = Phone
        fields = ('ddi', 'ddd', 'number')