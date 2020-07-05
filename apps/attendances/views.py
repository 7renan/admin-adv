from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
# models
from apps.attendances.models import Attendance

# forms
from apps.attendances.forms import AttendanceCreate


class AttendanceList(LoginRequiredMixin, ListView):
    template_name = 'attendance/attendance_list.html'
    model = Attendance
    paginate_by = 50
    context_object_name = 'attendances'


class AttendanceCreate(LoginRequiredMixin, CreateView):
    template_name = 'attendance/attendance_create.html'
    model = Attendance
    form_class = AttendanceCreate
    success_url = reverse_lazy('attendances:list')
