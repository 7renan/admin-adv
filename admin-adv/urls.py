
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts.urls')),
    path('customers/', include('apps.customers.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('attendances/', include('apps.attendances.urls')),
]
