from django.shortcuts import render
from django.views.generic import ListView
from customers.models import Customer


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