from django.db import models
from django.conf import settings


class Table(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование стола",
        help_text="Введите наименование стола",
    )
    description = models.CharField(
        max_length=150, verbose_name="Описание стола", help_text="Опишите стол"
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Вставьте фото стола",
    )
    price = models.IntegerField(
        verbose_name="Цена за стол", help_text="Введите цену за стол"
    )
    created_at = models.DateField(
        verbose_name="Дата создания стола в БД", help_text="Введите дату создания стола"
    )
    updated_at = models.DateField(
        verbose_name="Дата изменения стола в БД",
        help_text="Введите дату изменения стола",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров", help_text="Количество просмотров", default=0
    )

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"
        ordering = ["name"]


class Booking(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(default="example@example.com")
    date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания брони

    def __str__(self):
        return f"{self.name} - {self.date_time}"
