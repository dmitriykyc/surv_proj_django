from django.contrib.auth.forms import AuthenticationForm
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

