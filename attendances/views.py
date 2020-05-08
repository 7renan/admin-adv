from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

# models
from attendances.models import Attendance


class AttendanceList(LoginRequiredMixin, ListView):
    template_name = 'attendance/attendance_list.html'
    model = Attendance
    paginate_by = 50
    context_object_name = 'attendances'
