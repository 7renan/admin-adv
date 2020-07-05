from django.forms.models import ModelForm

# models
from apps.attendances.models import Attendance


class AttendanceCreate(ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'horary', 'topic', 'attended', ]


class AttendanceUpdate(ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'horary', ]
