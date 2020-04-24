from django.db import models


class Address(models.Model):
    street = models.CharField('Rua', max_length=120)
    number = models.CharField('Número', max_length=10)
    neighborhood = models.CharField('Bairro', max_length=80)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=50)
    complement = models.TextField('Complemento', null=True, blank=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.street
