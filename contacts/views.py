from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# models
from contacts.models import Contact


class ContactList(LoginRequiredMixin, ListView):
    template_name = 'contacts/contact_list.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        queryset = Contact.objects.all()
        search = self.request.GET.get('search', False)

        if search:
            queryset = queryset.filter(
                name__icontains=search
            )
        return queryset