from django.db import models
from django.contrib.auth.models import User


class Account(User):

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'