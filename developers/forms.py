from django import forms
from .models import *

class DevelopersForm(forms.ModelForm):
    class Meta :
        model=Developer
        fields='__all__'

class WeightageForm(forms.ModelForm):
    class Meta:
        model = Weightage
        fields = "__all__"