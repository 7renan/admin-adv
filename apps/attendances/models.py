from django.db import models
import datetime


class Attendance(models.Model):
    date = models.DateField('Data')
    horary = models.TimeField('Horário')
    topic = models.CharField('Assunto', max_length=300)
    attended = models.CharField('Atendido', max_length=150)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    @property
    def is_today(self):
        if self.date == datetime.date.today():
            return True

    def __str__(self):
        return str(self.date)

