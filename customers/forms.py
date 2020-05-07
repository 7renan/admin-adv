from django.forms.models import ModelForm
from customers.models import Customer


class CustomerFormCreate(ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'full_name', 'birth_date', 'cpf', 'rg', 'email', 'phone')
