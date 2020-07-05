from django.forms.models import ModelForm
from apps.addresses.models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('street','number','neighborhood','city','state','complement')