from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    detailed_desc = forms.CharField(max_length=1500, required=False, label='Detailed description',
                                    widget=widgets.Textarea)
    status = forms.ChoiceField(required=True, label='Status', choices=STATUS_CHOICES)
    finish_date = forms.DateField(required=False, label='Finish date', widget=forms.DateInput(attrs={
        'placeholder': 'YYYY-MM-DD'}))
