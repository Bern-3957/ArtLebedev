from django.db import models

# Create your models here.

class Worker(models.Model):
    id_code = models.CharField(max_length=24, verbose_name='id_code')
    created_at = models.CharField(max_length=100, verbose_name='Дата создания')
    person_id = models.IntegerField(verbose_name='id человека')
    name = models.CharField(max_length=30, verbose_name='Имя')
    secondName = models.CharField(max_length=30, verbose_name='Фамилия')
    lastName = models.CharField(max_length=30, verbose_name='Отчество')
    fullName = models.CharField(max_length=100, verbose_name='Полное имя')
    email = models.EmailField(blank=True, verbose_name='Почта')
    phone = models.IntegerField(verbose_name='Номер телефона')
    position = models.CharField(max_length=150, verbose_name='Должность')
    address = models.CharField(max_length=200, verbose_name='Адрес')

