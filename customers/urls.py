from django.urls import path
from customers import views

app_name = 'customers'

urlpatterns = [
    path('customers-list/', views.CustomersList.as_view(), name='customers_list'),
]