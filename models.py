from django.db import models


class Cardio(models.Model):
    form_data = models.JSONField(default=dict)

    # можно ли сделать пулл в json переназначением save?

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
