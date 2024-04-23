# resume_builder/forms.py

from django import forms
from .models import Profile  # Assuming Profile is your model

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'  # Or specify the fields you want to include in the form
