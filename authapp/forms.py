from django.forms import forms
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from authapp.models import SurveyUser


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = SurveyUser
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = SurveyUser
        fields = ('username', 'last_name', 'email', 'password1', 'password2', 'avatar', 'age')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''


    def clean_age(self):
        print(self)
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return age


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = SurveyUser
        fields = ('username', 'last_name', 'email', 'password', 'avatar', 'age')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()


    def clean_age(self):
        print(self)
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return age
