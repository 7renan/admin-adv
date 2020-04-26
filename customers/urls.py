from django.urls import path
from customers import views

app_name = 'customers'

urlpatterns = [
    path('customers-list/', views.CustomersList.as_view(), name='customers_list'),
    path('customers-create/', views.CustomerCreate.as_view() , name='customers_create'),
    path('customers-detail/<int:pk>', views.CustomerDetail.as_view(), name='customers_detail'),
]

