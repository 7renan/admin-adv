from django.urls import path
from apps.attendances import views

app_name = 'attendances'

urlpatterns = [
    path('list/', views.AttendanceList.as_view(), name='list'),
    path('create/', views.AttendanceCreate.as_view(), name='create'),
]