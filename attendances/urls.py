from django.urls import path
from attendances import views

app_name = 'attendances'

urlpatterns = [
    path('list/', views.AttendanceList.as_view(), name='list'),
]