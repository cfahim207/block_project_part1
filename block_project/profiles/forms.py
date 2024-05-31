from django import forms
from .models import Profiel

class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profiel
        fields= '__all__'