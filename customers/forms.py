from django.forms.models import ModelForm
from customers.models import Customer


class CustomerFormCreate(ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'full_name', 'address', 'birth_date', 'cpf', 'rg')
