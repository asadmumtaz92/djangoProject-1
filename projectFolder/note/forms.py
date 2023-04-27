from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {
            'title' : 'Enter note title:',
            'text' : 'Enter you note message:',
        }
        widgets = {
            'title': forms.TextInput(attrs=({'class': 'title-input mt10'})),
            'text': forms.Textarea(attrs=({'class': 'text-input mt30'}))
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if 'Django' not in title:
                raise ValidationError('We only accept notes about django')
            return title
