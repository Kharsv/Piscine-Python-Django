from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import HiddenInput, Textarea


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class FavouriteForm(forms.Form):
    article = forms.IntegerField(widget=HiddenInput(), required=True)

    def __init__(self, article, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if article is not None:
            self.fields['article'].initial = article


class PublishForm(forms.Form):
    title = forms.CharField(max_length=64, required=True)
    synopsis = forms.CharField(max_length=312, required=True)
    content = forms.CharField(widget=Textarea(), required=True)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",  "password1", "password2")