from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваше имя...'
    }))
    phone = forms.IntegerField(required=True, label='Номер', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваше номер...'
    }))
