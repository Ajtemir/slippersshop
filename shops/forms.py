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

class OrderForm(forms.Form):
    text = forms.CharField(max_length=100, required=True, label='Заказ', widget=forms.Textarea(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите...'
    }))
    name = forms.CharField(max_length=100, required=True, label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваше имя'
    }))
    address = forms.CharField(max_length=100, required=True, label='Адрес', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваш адрес'
    }))
    phone = forms.IntegerField(required=True, label='Номер', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваш номер'
    }))

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Поиск по названию', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите название товара...'
    }))

