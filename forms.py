from .models import Cardio, cardio_names
from django.forms import ModelForm, TextInput, Textarea, DateInput

cardio_names += ['title', 'check']


class CardioForm(ModelForm):
    class Meta:
        model = Cardio
        fields = cardio_names
        # widgets = {
        #     'task': Textarea(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Введите описание'
        #     })
        # }
