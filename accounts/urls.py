from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'accounts'

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
]