from django.db import models
# models
from addresses.models import Address


class Customer(models.Model):
    first_name = models.CharField('Primeiro nome', max_length=50)
    full_name = models.CharField('Nome completo', max_length=500)
    address = models.ForeignKey(Address, verbose_name='Endereço', on_delete=models.CASCADE)
    birth_date = models.DateField('Data de nascimento')
    cpf = models.CharField('CPF', max_length=20, unique=True)
    rg = models.CharField('RG', max_length=20, unique=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.full_name

