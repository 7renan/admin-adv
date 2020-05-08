from django.shortcuts import render
from django.views.generic import ListView, TemplateView, UpdateView
from customers.models import Customer
from django.urls import reverse_lazy
from django.shortcuts import redirect
# forms
from customers.forms import CustomerFormCreate, CustomerFormUpdate
from addresses.forms import AddressForm
from contacts.forms import PhoneFormCreate
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
        context['form_phone'] = PhoneFormCreate(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        customer_form = context['form']
        form_address = context['form_address']
        form_phone = context['form_phone']

        if all((customer_form.is_valid(), form_address.is_valid(), form_phone.is_valid())):
            address = form_address.save()
            customer_form.instance.address = address
            phone = form_phone.save()
            customer_form.instance.phone = phone
            customer = customer_form.save()
            customer.save()
            return redirect(reverse_lazy('customers:customers_list'))
        return self.render_to_response(context)


class CustomerDetail(TemplateView):
    template_name = 'customers/customers_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        context['customer'] = Customer.objects.filter(
            pk=self.kwargs['pk']
        ).first()
        return context


class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerFormUpdate
    template_name = 'customers/customers_update.html'

    def get_success_url(self):
        return reverse_lazy('customers:customers_detail', kwargs={'pk': self.get_object().pk})
