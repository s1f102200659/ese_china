from django import forms

class TranslationForm(forms.Form):
    input_text = forms.CharField()