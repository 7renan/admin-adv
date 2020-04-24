from django.db import models


class Phone(models.Model):
    ddd = models.CharField('DDD', max_length=2)
    number = models.CharField('Número', max_length=11)

    def __str__(self):
        return self.number


class Contact(models.Model):
    name = models.CharField('Nome', max_length=150)
    email = models.EmailField('Email')
    phone = models.ForeignKey(Phone, verbose_name='Telefone' , on_delete=models.CASCADE)

    def __str__(self):
        return self.name


