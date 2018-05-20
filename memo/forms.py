from django.forms import ModelForm, TextInput
from .models import Memo


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': TextInput(attrs={'class': 'memo_form'})
        }
