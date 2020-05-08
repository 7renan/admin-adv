
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('customers/', include('customers.urls')),
    path('contacts/', include('contacts.urls')),
    path('attendances/', include('attendances.urls')),
]
