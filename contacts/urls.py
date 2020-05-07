from django.urls import path
from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('contact-list/', views.ContactList.as_view(), name='contact_list'),
]


