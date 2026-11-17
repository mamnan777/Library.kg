from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=50)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Телефон', max_length=20)
    country = forms.CharField(label='Страна', max_length=50)
    address = forms.CharField(label='Адрес', max_length=255)
    gender = forms.ChoiceField(label='Пол', choices=Profile.GENDER_CHOICES)
    occupation = forms.CharField(label='Профессия', max_length=100)
    bio = forms.CharField(label='О себе', widget=forms.Textarea, required=False)
    birth_date = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    city = forms.CharField(label='Город', max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Profile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                birth_date=self.cleaned_data['birth_date'],
                city=self.cleaned_data['city'],
                country=self.cleaned_data['country'],
                address=self.cleaned_data['address'],
                gender=self.cleaned_data['gender'],
                occupation=self.cleaned_data['occupation'],
                bio=self.cleaned_data['bio'],
            )
        return user


class LoginForm(AuthenticationForm):
    captcha = forms.IntegerField(label='Капча')

    def clean_captcha(self):
        answer = self.cleaned_data['captcha']
        if answer != self.request.session.get('captcha_answer'):
            raise forms.ValidationError('Неверный ответ на капчу')
        return answer