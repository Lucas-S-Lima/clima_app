from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50, null=True, unique=True, verbose_name='Cidade')

    def __str__(self):
        return self.city


class Alert(models.Model):
    OPERATORS = [
        ('=', 'Igual a'),
        ('>', 'Maior que'),
        ('<', 'Menor que'),
    ]

    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, verbose_name='Cidade')
    operator = models.CharField(max_length=1, choices=OPERATORS, default='=', verbose_name='Operador')
    temperature = models.FloatField(verbose_name='Temperatura')
    message = models.TextField(verbose_name='Mensagem')
    active = models.BooleanField(default=True, verbose_name='Ativo')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado em')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.message} - {self.temperature} - {self.city}"


class Temperature(models.Model):

    temperature = models.FloatField(verbose_name='Temperatura')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Cidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.temperature} - {self.city} ºC"
