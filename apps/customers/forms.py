from django.forms.models import ModelForm
from apps.customers.models import Customer


class CustomerFormCreate(ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'full_name', 'birth_date', 'cpf', 'rg', 'email', 'phone')


class CustomerFormUpdate(ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'rg', 'cpf', 'birth_date')