from django.db import models


class Phone(models.Model):
    ddi = models.CharField('DDI', max_length=2, blank=True, default=55)
    ddd = models.CharField('DDD', max_length=2, blank=True)
    number = models.CharField('Número', max_length=11, blank=True)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return self.number


class Contact(models.Model):
    name = models.CharField('Nome', max_length=150)
    email = models.EmailField('Email')
    phone = models.ForeignKey(Phone, verbose_name='Telefone', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name

