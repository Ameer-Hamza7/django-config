from django.forms import ModelForm
from .models import DummyModel

class DummyModelForm(ModelForm):
    class Meta:
        model = DummyModel
        fields = '__all__'
