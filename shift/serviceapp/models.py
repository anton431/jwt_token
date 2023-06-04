from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
import jwt


class Person(models.Model):
    login = models.CharField('Логин', max_length=17, unique=True)
    date_up = models.DateField('Дата повышения', blank=True)
    salary = models.IntegerField('Зарплата, $', max_length=17, blank=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.login
