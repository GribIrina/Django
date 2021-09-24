from django.db import models
from .excel2form import cardio_fields

cardio_names = []


class Cardio(models.Model):
    title = models.TextField('Название', default='Untitled')
    check = models.TextField('тестируемое', default='Untitled')
    for field in cardio_fields:
        name = field['name']
        if field['type'] == 'text':
            cardio_names.append(name)
            globals()[name] = models.TextField(name, default=field['description'])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
