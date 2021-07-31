from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django import forms

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваше имя пользователя'
    }))

    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваше имя пользователя'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Данный пользователь не активен')
        return super().clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control input-text',
                                   'placeholder': 'Напишите ваше имя пользователя'
                               }))

    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваше имя'
    }))

    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите вашу фамилию'
    }))

    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите вашу почту'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Напишите ваш пароль'
    }))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control input-text',
        'placeholder': 'Подтвердите ваш пароль'
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']



