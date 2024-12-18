from django import forms
from django.utils import timezone
from .models import Robot
from django.core.exceptions import ValidationError


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = '__all__'

    def clean_created(self):
        date_value = self.cleaned_data['created']
        if date_value.date() > timezone.now().date():
            raise ValidationError('Created date cant be greater than today')
        return date_value
