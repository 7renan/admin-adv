from django.shortcuts import render
# decorators
from django.contrib.auth.decorators import login_required

# models
from apps.customers.models import Customer


@login_required
def dashboard(request):
    number_customers = Customer.objects.all().count()
    context = {
        'number_customers':number_customers,
    }
    return render(request, 'accounts/dashboard.html', context)
