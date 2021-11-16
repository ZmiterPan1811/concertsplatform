from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Event(models.Model):

    performer = models.CharField(max_length=255, verbose_name="Исполнители")
    amount = models.IntegerField(verbose_name="Количество билетов")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Стоимость билета")
    date = models.DateTimeField(verbose_name="Дата проведения")
    address = models.CharField(max_length=150, verbose_name="Место проведения")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    map = models.TextField(blank=True, verbose_name="Местоположение")

    def __str__(self):
        return self.performer

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-id']


class Concert(Event):
    title = models.CharField(max_length=255, verbose_name="Название")
    composer = models.CharField(max_length=150, verbose_name="Композитор")
    voicetype = models.CharField(blank=True, max_length=100, verbose_name="Тональность исполнителя")

    def __str__(self):
        return self.title


class Show(Event):
    headliner = models.CharField(max_length=255, verbose_name="Хедлайнер")
    route = models.TextField(verbose_name="Как добраться")

    def __str__(self):
        return self.headliner


class Party(Event):
    constraint = models.IntegerField(verbose_name="Возрастное ограничение")

    def __str__(self):
        return "{}".format(self.performer)



