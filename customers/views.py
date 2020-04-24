from django.shortcuts import render
from django.views.generic import ListView
from customers.models import Customer


class CustomersList(ListView):
    template_name = 'customers/customers_list.html'
    context_object_name = 'customers'
    model = Customer

    def get_queryset(self):
        pass
