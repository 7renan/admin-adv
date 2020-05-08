from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class AttendanceList(TemplateView):
    template_name = 'attendance/attendance_list.html'
