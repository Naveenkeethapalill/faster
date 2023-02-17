from django import forms
from . models import Test

class TestForm(forms.ModelForm):
    class Meta:
        model=Test
        fields='__all__'
        labels={
            'name':'enter name',
            'email':'enter email',
            'service':'select service',
        }