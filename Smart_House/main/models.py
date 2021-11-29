from django.db import models


class Controls(models.Model):
    name_controller = models.CharField(
        'Пристрій керування',
        max_length=150,
    )
    has_item = models.IntegerField(
        'Кількість підключених предметів до цього пристрою'
    )
    # image = models.ImageField(
    #     'Зображення засобів керування',
    #     upload_to='img/controllers'
    # )

    def __str__(self):
        return self.name_controller

    def get_absolute_url(self):
        return f'/controllers/{self.id}'

    class Meta:
        verbose_name = 'Засіб керування'
        verbose_name_plural = 'Засоби керування'


class Items(models.Model):
    name = models.CharField(
        'Назва елементу',
        max_length=255,
    )
    title = models.CharField(
        'Короткий опис',
        max_length=255,
    )
    # image = models.ImageField(
    #     'Зображення пристроїв',
    #     upload_to='img/items'
    # )
    controller = models.ForeignKey(
        Controls,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/items/{self.id}'

    class Meta:
        verbose_name = 'Пристрій'
        verbose_name_plural = 'Пристрої'
