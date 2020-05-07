from django.shortcuts import render
from django.views.generic import TemplateView , ListView

# models
from contacts.models import Contact


class ContactList(ListView):
    template_name = 'contacts/contact_list.html'
    model = Contact
    context_object_name = 'contacts'

