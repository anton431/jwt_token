from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
import jwt


class Person(models.Model):
    login = models.CharField('Логин', max_length=17, unique=True)
    password = models.CharField('Пароль', max_length=17)
    date_up = models.DateTimeField('Дата повышения')
    salary = models.SmallIntegerField('Зарплата, $')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.login
