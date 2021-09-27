from .models import Cardio
from django.forms import ModelForm, CharField, JSONField
import sys
sys.path.insert(0, '/Users/grib/PycharmProjects/GKMP/HCM/HCM')
from settings import cardio_fields, cardio_names
# не сработал метод импорта с .HCM.HCM.settings


class CardioForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CardioForm, self).__init__(*args, **kwargs)
        for field in cardio_fields:
            field_name = field['name']
            display_name = field['description']
            self.fields[field_name] = CharField(label=display_name, max_length=10)

# научиться сохранять данные в form_data

    class Meta:
        model = Cardio()
        fields = []

    #     # widgets = {
    #     #     'task': Textarea(attrs={
    #     #         'class': 'form-control',
    #     #         'placeholder': 'Введите описание'
    #     #     })
    #     # }
