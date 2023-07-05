from .models import CbvModel
from django.forms import ModelForm

class CbvForm(ModelForm):
    class Meta:
        model = CbvModel
        fields = '__all__'