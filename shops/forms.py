from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.IntegerField(required=True)