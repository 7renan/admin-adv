from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from customers.models import Customer
# forms
from customers.forms import CustomerFormCreate
from addresses.forms import AddressForm
from contacts.forms import ContactFormCreate


class CustomersList(ListView):
    template_name = 'customers/customers_list.html'
    context_object_name = 'customers'
    model = Customer

    def get_queryset(self):
        queryset = Customer.objects.all()
        search = self.request.GET.get('search', False)
        if search:
            queryset = Customer.objects.filter(
                full_name__icontains=search
            )
        return queryset


class CustomerCreate(TemplateView):
    template_name = 'customers/customers_create.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerCreate, self).get_context_data(**kwargs)
        context['form'] = CustomerFormCreate(self.request.POST or None)
        context['form_address'] = AddressForm(self.request.POST or None)
        context['form_contact'] = ContactFormCreate(self.request.POST or None)
        return context

    def post(self):
        pass


