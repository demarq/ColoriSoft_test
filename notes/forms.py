from django import forms
from.models import Notes


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=50, label='Заголовок')
    text = forms.CharField(max_length=300, widget=forms.Textarea, label='Текст')

    def clean_title(self):
        title = self.cleaned_data['title']
        if title is not '':
            return title
        else:
            raise forms.ValidationError('Title cant be empty.')

    def clean_text(self):
        text = self.cleaned_data['text']
        if text is not '':
            return text
        else:
            raise forms.ValidationError('Title cant be empty.')

    def save(self):
        notes = Notes(**self.cleaned_data)
        notes.unique_symbols = notes.calc_uniq_symbols(self.cleaned_data['text'])
        notes.save()
        return True
