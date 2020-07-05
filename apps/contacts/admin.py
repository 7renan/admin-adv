from django.contrib import admin
from apps.contacts.models import Contact, Phone

admin.site.register(Phone)
admin.site.register(Contact)

